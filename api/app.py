import datetime
from os import environ as env

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from dotenv import find_dotenv, load_dotenv
from flask_migrate import Migrate

from database import db, UserModel
from auth import hash_password, verify_password

### ----- Configuration ----- ###

# Load environment variables from .env file
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

# Flask setup
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{env.get('MYSQL_USER')}:{env.get('MYSQL_PASSWORD')}@{env.get('HOSTNAME')}:3306/{env.get('MYSQL_DATABASE')}"
app.secret_key = env.get("APP_SECRET_KEY")

# JWT setup
jwt = JWTManager(app)

CORS(app, supports_credentials=True, origins=env.get("CORS_ALLOWED_ORIGINS").split(","))
db.init_app(app)
migrate = Migrate(app, db)

### ----- Routes ----- ###

@app.route("/health", methods=["GET"])
def health():
  return jsonify({"message": "Healthy"}), 200

@app.route("/health_protected", methods=["GET"])
@jwt_required()
def health_protected():
  user = UserModel.query.get(get_jwt_identity())
  return jsonify({"message": "Healthy", "user": user.username}), 200

# Authentication / Registration
@app.route("/login", methods=["POST"])
def login():
  data = request.get_json()
  username = data.get("username")
  password = data.get("password")

  user = UserModel.query.filter_by(username=username).one_or_none()
  if not user:
    return jsonify({"error": "Invalid username or password"}), 401
  
  if not verify_password(password, user.password):
    return jsonify({"error": "Invalid username or password"}), 401
  
  expires = datetime.timedelta(days=1)
  access_token = create_access_token(identity=user.id, expires_delta=expires)
  return jsonify({
    "access_token": access_token
  }), 200

@app.route("/register", methods=["POST"])
def register():
  data = request.get_json()
  email = data.get("email")
  username = data.get("username")
  password = data.get("password")

  if UserModel.query.filter_by(username=username).one_or_none():
    return jsonify({"error": "Username already exists"}), 400

  if UserModel.query.filter_by(email=email).one_or_none():
    return jsonify({"error": "Email already exists"}), 400

  hashed_password = hash_password(password)
  user = UserModel(email=email, username=username, password=hashed_password, created_at=datetime.datetime.now())
  db.session.add(user)
  db.session.commit()

  return jsonify({"message": "User created successfully"}), 201