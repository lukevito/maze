import yaml
import subprocess
from kubernetes import client
import prometheus_client
import time
import os

def load_config(config_filename):
    config_file = os.path.join(os.getcwd(), config_filename)
    with open(config_file, "r") as f:
        return yaml.safe_load(f)

def build_images():
    config = load_config("config.yaml")

    kafka_file = os.path.join(os.getcwd(), "app-kafka/Dockerfile")
    web_file = os.path.join(os.getcwd(), "app-web/Dockerfile")

    subprocess.run(
        ["docker", "build", "-t", "maze-app-kafka", "-f",kafka_file, "."], cwd="app-kafka"
    )
    subprocess.run(
        ["docker", "build", "-t","maze-app-web", "-f", web_file, "."], cwd="app-web"
    )

def deploy_to_kubernetes():
    config = load_config("config.yaml")

    k8s_client = client.ApiClient()
    apps_v1 = client.AppsV1Api(k8s_client)

    for deployment in config["deployments"]:
        with open(deployment["file"], "r") as f:
            deployment_definition = yaml.safe_load(f)
        apps_v1.create_namespaced_deployment(
            namespace="default", body=deployment_definition
        )

    for service in config["services"]:
        with open(service["file"], "r") as f:
            service_definition = yaml.safe_load(f)
        apps_v1.create_namespaced_service(
            namespace="default", body=service_definition
        )

def run_docker_compose():
    """
    Uruchamia komendę docker-compose up za pomocą subprocess.
    """
    subprocess.run(["docker-compose", "up", "-d"], check=True)

metrics = {
    "cpu_usage": prometheus_client.Gauge("cpu_usage", "CPU usage of the application"),
    "memory_usage": prometheus_client.Gauge("memory_usage", "Memory usage of the application"),
}

def monitor_applications():
    prometheus_client.start_http_server(8000)  # Start Prometheus endpoint

    while True:
        # Implement logic to collect application metrics
        # Update relevant gauges with collected values
        # Replace with your actual data collection logic
        metrics["cpu_usage"].set(0.5)  # Example
        metrics["memory_usage"].set(100)  # Example
        time.sleep(10)  # Collect metrics periodically

if __name__ == "__main__":
    build_images()
    run_docker_compose()
    # deploy_to_kubernetes()
    monitor_applications()
