# import kubernetes client, and config
from kubernetes import client, config

# Load Kubernetes configuration
config.load_kube_config()

# Create a Kubernetes API client
api_client = client.ApiClient()

# Define the Deployment
deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="flask-app"),
    spec=client.V1DeploymentSpec(
        replicas=3,
        selector=client.V1LabelSelector(
            match_labels={"app": "flask-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "flask-app"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="my-flask-container",
                        image="accountIDhere.dkr.ecr.us-east-1.amazonaws.com/my-cloud-native-repo:latest",
                        ports=[client.V1ContainerPort(container_port=5000)]
                    )
                ]
            )
        )
    )
)
                   
# Create the Deployment
api_instance = client.AppsV1Api(api_client)
api_instance.create_namespaced_deployment (
    namespace="default",
    body=deployment
)

# Define the Service
service = client.V1Service(
    metadata=client.V1ObjectMeta(name="my-flask-service"),
    spec=client.V1ServiceSpec(
        selector={"app": "flask-app"},
        ports=[client.V1ServicePort(port=5000)]
    )
)        

# Create the Service
api_instance = client.CoreV1Api(api_client)
api_instance.create_namespaced_service(
    namespace="default",
    body=service
)
