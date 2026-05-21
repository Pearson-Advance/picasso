"""
Mapping of service identifiers to their corresponding Docker image environment variable names.

Keys:
    - "openedx": Open edX platform container
    - "mfe": Micro-frontend container
    - "aspects-superset": Superset-based reporting container
    - "discovery": Discovery service
    - "ecommerce": Ecommerce service
    - "ecommerce-worker": Ecommerce worker service
    - "enterprise-catalog": Enterprise catalog service

Values:
    Environment variable names used to specify Docker images for each service.
"""
service_tag_map = {
  "openedx": "DOCKER_IMAGE_OPENEDX",
  "openedx-dev": "DOCKER_IMAGE_OPENEDX_DEV",
  "mfe": "MFE_DOCKER_IMAGE",
  "aspects-superset": "DOCKER_IMAGE_SUPERSET",
  "discovery": "DISCOVERY_DOCKER_IMAGE",
  "ecommerce": "ECOMMERCE_DOCKER_IMAGE",
  "ecommerce-worker": "ECOMMERCE_WORKER_DOCKER_IMAGE",
  "enterprise-catalog": "ENTERPRISE_CATALOG_DOCKER_IMAGE",
}
