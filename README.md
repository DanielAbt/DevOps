# DevOps Training

Local Infraestructure...

The Docker Compose file defines a local environment for DevOps practices

### Nexus:

Create and install local nexus server.

1. Create volume for persistent data.
   1. ```
      docker volume create nexus_data
      ```
2. Get default admin password.
   1. ```
      docker exec -it nexus3 cat /nexus-data/admin.password
      ```
3. Create an user to use in local and ci/cd workflow.
4. Create local registry.
