import secrets
import time

def generate_password(n):
  return secrets.token_urlsafe(n)

def write_env_file():
  with open(".env", "w") as f:
    f.write(f"CORS_ALLOWED_ORIGINS={CORS_ALLOWED_ORIGINS}\n")
    f.write(f"APP_SECRET_KEY={APP_SECRET_KEY}\n")
    f.write(f"INITIAL_ADMIN_USER={INITIAL_ADMIN_USER}\n")
    f.write(f"INTIAL_ADMIN_PASSWORD={INTIAL_ADMIN_PASSWORD}\n")
    f.write(f"MYSQL_DATABASE={MYSQL_DATABASE}\n")
    f.write(f"MYSQL_USER={MYSQL_USER}\n")
    f.write(f"MYSQL_ROOT_PASSWORD={MYSQL_ROOT_PASSWORD}\n")
    f.write(f"MYSQL_PASSWORD={MYSQL_PASSWORD}\n")
    f.write(f"HOSTNAME={HOSTNAME}\n")

if __name__ == "__main__":

  initial_admin_user = input("Enter the initial admin username (default: admin): ")
  mysql_database = input("Enter the MySQL database name (default: appdb): ")
  mysql_user = input("Enter the MySQL user name (default: appuser): ")
  hostname = input("Enter the MySQL hostname (default: localhost): ")
  cors = input("Enter the CORS allowed origins (default: http://localhost:3000,http://localhost:5000,http://localhost:5173): ")

  CORS_ALLOWED_ORIGINS=cors if cors else "http://localhost:3000,http://localhost:5000,http://localhost:5173"
  APP_SECRET_KEY=generate_password(32)
  INITIAL_ADMIN_USER=initial_admin_user if initial_admin_user else "admin"
  INTIAL_ADMIN_PASSWORD=generate_password(10)
  MYSQL_DATABASE=mysql_database if mysql_database else "appdb"
  MYSQL_USER=mysql_user if mysql_user else "appuser"
  MYSQL_ROOT_PASSWORD=generate_password(32)
  MYSQL_PASSWORD=generate_password(16)
  HOSTNAME=hostname if hostname else "localhost"

  write_env_file()
  # clear screen for better visibility
  print("\033[H\033[J")
  print(".")
  time.sleep(0.75)
  print("\033[H\033[J")
  print("..")
  time.sleep(0.75)
  print("\033[H\033[J")
  print("...")
  time.sleep(0.75)
  print("\033[H\033[J")

  print("Your application variables have been set.")
  print(" ------------------------ ")
  print()
  print(" ### APPLICATION ### ")
  print()
  print(f"CORS_ALLOWED_ORIGINS = {CORS_ALLOWED_ORIGINS}")
  print(f"INITIAL_ADMIN_USER = {INITIAL_ADMIN_USER}")
  print(f"INTIAL_ADMIN_PASSWORD = {INTIAL_ADMIN_PASSWORD}")
  print()
  print(' ------------------------')
  print()
  print(" ### DATABASE ### ")
  print()
  print(f"HOSTNAME = {HOSTNAME}")
  print(f"MYSQL_DATABASE = {MYSQL_DATABASE}")
  print(f"MYSQL_USER = {MYSQL_USER}")
  print(f"MYSQL_PASSWORD = {MYSQL_PASSWORD}")
  print(" ------------------------ ")