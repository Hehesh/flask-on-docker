import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MEDIA_FOLDER = os.path.join(basedir, "media")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
