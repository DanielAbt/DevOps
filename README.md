# DevOps Training



Project Structure:

```plaintext
├── insfraestructure
│   ├── docker-compose.yml
│   ├── nexus
│   |   └── Dockerfile
│   └── jenkins
│       └── Dockerfile
├── apps
│   └── ip_app
└── README.md

```

### Apps:

### Infraestructure:

The Docker Compose file defines a local environment for DevOps practices

#### Nexus:

Create and install local nexus server.

1. Create volume for persistent data.
   1. ```
      docker volume create nexus-data
      ```
2. Get default admin password.
   1. ```
      docker exec -it nexus3 cat /nexus-data/admin.password
      ```
3. Create an user to use in local and ci/cd workflow.
4. Create local registry.

### Jenkins:

Create and install local jenkins server.

1. Create volume for persistent data.

   1. ```
      docker volume create jenkins-data
      ```
2. Get default admin password.

   1. ```
      docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword
      ```
3. Install and update plugins.
