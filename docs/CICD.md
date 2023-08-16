## Continuous Integration and Continuous Deployment

Pre-requisites

- Git branching Strategy
  - GitFlow Model
- Code Quality
  - Formatting
  - Code Complexity
  - Code Smells
- Testing Strategy
  - Unit Test
  - Test Coverage > 90%
  - Functional ATDD Test
- Deployment Strategy
  - Infrastructure as Code
  - Blue/Green Deployment
  - Canary Deployment
  - Rollback
- Security Testing Strategy
  - Software Composition Analysis
  - Static Analysis Security Testing
  - Dynamic Analysis Security Testing
  - Container Vulnerabilities
  - Code Vulnerabilities
  - Infrastructure Vulnerabilities
- Software Versioning Strategy
  - Semantic Versioning

## CICD Stages

    1. Git checkout from feature branch
    2. Code Quality
        * Complexity
        * Format
    3. Unit Test
    4. Build
    5. SCA Analysis
    6. SAST
    7. Scan Container Vulnerability
    8. QA Deploy
    9. ATDD Test
    11. DAST
    12. Release Approval
    13. Prod Deploy
    14. Rollback
