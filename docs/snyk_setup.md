# Snyk Setup

## IDE Plugin Installing Scanning

1. Install `snyk` extension for `vscode`
![snyk plugin extension](images/vscode_snyk_plugin_install.png)

2. Initiate `snyk` scan inside `vscode`
![snyk initiate scan](images/vscode_snyk_scan.png)

3. `snyk` scans for 
    1. Open Source Security - Find and automatically fix open-source vulnerabilities
    2. Code Security - Find and fix vulnerabilities in your application code
    3. Configurations - Find and fix insecure configurations
    4. Code Quality - 
    Identify issues and view recommended fixes. Once fixed, rescan

> NOTE:- Action Required -  Ability to pass snyk sast scan merging PR for releasing software.  

References
> https://docs.snyk.io/getting-started/getting-started-with-snyk-free-team-plan

## snyk-cli to scan projects

## mac
```
brew tap snyk/tap && brew install snyk
```

1. Authenticate with `synk` 

![synk auth cli cmd](images/synk_auth_cli_cmd.png)

Redirected from CLI to web App
![synk redirect auth](images/snyk_redirect_auth.png)

Confirm web authentication
![synk auth condirm](images/synk_auth_confirm.png)

Authentication success
![synk auth success](images/synk_auth_success.png)

2. Scan project with synk
![synk test](images/snyk_test.png)

3. Monitor scanned projects with synk 
![synk monitor](images/synk_monitor.png)

4. Scan containers with synk
![synk container test](images/synk_container_test.png)
![synk container test](images/synk_container_test2.png)

5. Test code with synk
![synk code test](images/synk_code_test.png)

6. Check for log4Shell issues with synk
![synk log4Shell](images/synk_log4shell.png)

