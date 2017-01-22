# zops.jenkins_jobs

Manage the creation of jenkins jobs.

Organize your [Jenkins](jenkins.io) jobs right inside your code.

A typical projetct usinhg zops.jenkins_jobs directory would look like this:

```
/jenkins-jobs
  Jenkinsfile
  branch.yml
  jenkins-jobs.ini
```

### branch.yml

```YAML
- job:
    name: {setup.name}__{git.branch}
    project-type: pipeline
    pipeline:
      script-path: jenkins-jobs/Jenkinsfile
      scm:
        - git:
            url: '{setup.url}'
            credentials-id: 'c8d28ec9-5d38-49a1-8b61-30db890bbb34'
            skip-tag: true
            wipe-workspace: false
            branches:
              - '*/{git.branch}'
```

* The {setup.name} and {setup.url} variable are obtained from setup.py;
* The {git.branch} variable is obtained from the git repository;
```

With the following command line you can create the job in your Jenkins server:

```bash
$ zops jobs create
```
