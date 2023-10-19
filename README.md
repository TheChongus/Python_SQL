# Storing Database Credentials as Environment Variables
---
### On Windows:

    Open the Start menu and search for "Environment Variables."
    Click on "Edit the system environment variables."

### For User Variables:

    In the "System Properties" window, click the "Environment Variables" button.
    Under "User variables," click "New" to add a new environment variable.
    Set the "Variable name" (e.g., DB_HOST) and the "Variable value" (e.g., your actual host address).
    Repeat this process for other credentials like DB_USER, DB_PASSWORD, and DB_DATABASE.

### For System Variables:

    To set system-wide environment variables, you can do the same in the "System variables" section.

## On macOS and Linux:

You can set environment variables in your shell profile, such as ~/.bashrc, ~/.bash_profile, or ~/.zshrc. Here's how you can do it in a terminal:

    Open a terminal.

    Open your shell profile in a text editor, for example, using nano:

    'nano ~/.bashrc'

    Add lines like the following to set your environment variables:

    'export DB_HOST="your_host_address"'
    'export DB_USER="your_username"'
    'export DB_PASSWORD="your_password"'
    'export DB_DATABASE="your_database_name"'
    'export DB_PORT="your_port_number"'

Save the file and exit the text editor.

To apply these changes immediately, you can run:

    'source ~/.bashrc'

These environment variables are now available for your Python scripts to access, as shown in the previous response. Just replace 'DB_HOST', 'DB_USER', 'DB_PASSWORD', and 'DB_DATABASE' with the actual names of your environment variables.

---