import hashlib
import inspect
import magic
import math
import os
import re
import time
import werkzeug
from abc import abstractmethod
from datetime import datetime, timedelta, timezone
from sqlalchemy.dialects.mysql import (
    BIGINT,
    MEDIUMINT,
    SMALLINT,
    TINYINT,
    VARBINARY,
    DATE,
    BLOB,
)
from sqlalchemy.ext.declarative import declared_attr
from src import setting
from src.util.util import util
from .entity import entity
from .timestamp_mixin_entity import timestamp_mixin_entity
from .prefectures_entity import prefectures_entity
from .zip_addresses_entity import zip_addresses_entity
from .contact_methods_entity import contact_methods_entity
from .knew_triggers_entity import knew_triggers_entity
from .birth_days_entity import birth_days_entity
from .jobs_entity import jobs_entity
from .sexes_entity import sexes_entity
from .pre_users_entity import pre_users_entity
from .users_entity import users_entity
from .user_contact_methods_entity import user_contact_methods_entity
from .user_knew_triggers_entity import user_knew_triggers_entity
