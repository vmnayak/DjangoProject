import os
from django.core.management import call_command

def reset_migrations(app_name):
    # Step 1: Delete migration files
    migrations_dir = os.path.join(app_name, 'migrations')
    for filename in os.listdir(migrations_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            os.remove(os.path.join(migrations_dir, filename))

    # Step 2: Reset database schema
    call_command('migrate', app_name, 'zero')
    call_command('flush')
    call_command('makemigrations', app_name)
    call_command('migrate', app_name)

if __name__ == "__main__":
    app_name = 'base'  # Replace with your app name
    reset_migrations(app_name)
