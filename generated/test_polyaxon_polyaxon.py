import sys
_module = sys.modules[__name__]
del sys
helm = _module
polyaxon = _module
agents = _module
agent = _module
base = _module
converter = _module
manager = _module
spawners = _module
async_spawner = _module
spawner = _module
api = _module
builds = _module
builder = _module
generator = _module
dockerfile = _module
cli = _module
admin = _module
auth = _module
check = _module
completion = _module
components = _module
docker = _module
initializer = _module
notifier = _module
proxies = _module
sidecar = _module
tuner = _module
config = _module
dashboard = _module
errors = _module
executor = _module
conda = _module
k8s = _module
platform = _module
init = _module
operations = _module
port_forward = _module
projects = _module
run = _module
upload = _module
version = _module
client = _module
decorators = _module
can_log_event = _module
can_log_outputs = _module
is_managed = _module
no_op = _module
offline = _module
handlers = _module
conf = _module
handler = _module
impersonate = _module
project = _module
transport = _module
http_transport = _module
periodic_transport = _module
retry_transport = _module
socket_transport = _module
threaded_transport = _module
utils = _module
workers = _module
base_worker = _module
periodic_worker = _module
queue_worker = _module
config_reader = _module
spec = _module
connections = _module
aws = _module
s3 = _module
azure = _module
azure_blobstore = _module
gcp = _module
gcs = _module
getter = _module
kinds = _module
reader = _module
schemas = _module
k8s_resources = _module
constants = _module
containers = _module
contexts = _module
names = _module
pull_policy = _module
statuses = _module
deploy = _module
operators = _module
cmd_operator = _module
compose = _module
kubectl = _module
pip = _module
celery = _module
deployment = _module
deployment_types = _module
email = _module
ingress = _module
intervals = _module
rbac = _module
root_user = _module
security_context = _module
service = _module
service_types = _module
ssl = _module
env_vars = _module
getters = _module
component = _module
user = _module
keys = _module
exceptions = _module
git = _module
async_manager = _module
custom_resources = _module
crd = _module
operation = _module
events = _module
k8s_schemas = _module
monitor = _module
namespace = _module
pods = _module
run_instance = _module
lifecycle = _module
logger = _module
main = _module
managers = _module
ignore = _module
notifiers = _module
discord_webhook = _module
hipchat_webhook = _module
mattermost_webhook = _module
pagerduty_webhook = _module
slack_webhook = _module
webhook = _module
parser = _module
pkg = _module
plugins = _module
sentry = _module
polyaxonfile = _module
params = _module
specs = _module
compiled_operation = _module
libs = _module
validator = _module
sections = _module
polyboard = _module
artifacts = _module
paths = _module
logging = _module
polyflow = _module
cache = _module
component_reference = _module
container = _module
dags = _module
early_stopping = _module
policies = _module
environment = _module
io = _module
matrix = _module
bayes = _module
grid_search = _module
hyperband = _module
hyperopt = _module
iterative = _module
mapping = _module
random_search = _module
mounts = _module
artifacts_mounts = _module
notifications = _module
optimization = _module
ops_params = _module
references = _module
dag = _module
hub = _module
mixin = _module
path = _module
url = _module
dask = _module
flink = _module
job = _module
kubeflow = _module
clean_pod_policy = _module
mpi_job = _module
pytorch_job = _module
replica = _module
tf_job = _module
patch = _module
ray = _module
spark = _module
schedule = _module
cron = _module
exact_time = _module
interval = _module
repeatable = _module
termination = _module
trigger_policies = _module
polyplot = _module
run_plot = _module
polypod = _module
common = _module
accelerators = _module
container_resources = _module
setter = _module
stores = _module
volumes = _module
compiler = _module
converters = _module
pytroch_job = _module
resolver = _module
resolvers = _module
core = _module
store = _module
mixins = _module
pod = _module
polytune = _module
dist = _module
iteration = _module
search_managers = _module
bayesian_optimization = _module
acquisition_function = _module
optimizer = _module
space = _module
pql = _module
generators = _module
gateway = _module
streams = _module
uwsgi = _module
buffering = _module
charset = _module
error_page = _module
dns = _module
healthz = _module
redirect = _module
services = _module
urls = _module
gzip = _module
listen = _module
locations = _module
gunicorn = _module
timeout = _module
authentication = _module
log_handler = _module
resources = _module
agent_config = _module
cli_config = _module
client_config = _module
proxies_config = _module
fields = _module
dict_or_str = _module
docker_image = _module
float_or_str = _module
indexed_dict = _module
int_or_str = _module
obj_list_obj = _module
ref_or_obj = _module
str_or_fct = _module
swagger = _module
tensor = _module
uuids = _module
types = _module
event = _module
image = _module
uri = _module
wasb = _module
ephemeral = _module
headers = _module
settings = _module
outputs = _module
summaries = _module
base_store = _module
local_store = _module
polyaxon_store = _module
app = _module
endpoints = _module
controllers = _module
archived_logs = _module
k8s_crd = _module
k8s_logs = _module
tasks = _module
logs = _module
notification = _module
tracking = _module
contrib = _module
fastai = _module
keras = _module
tensorboard = _module
tensorflow = _module
events_processors = _module
gpu_processor = _module
psutil_processor = _module
writer = _module
bool_utils = _module
cached_property = _module
click_utils = _module
cmd = _module
code_reference = _module
date_utils = _module
enums_utils = _module
env = _module
formatting = _module
hashing = _module
http = _module
http_utils = _module
humanize = _module
imports = _module
indentation = _module
list_utils = _module
log_levels = _module
manager_interface = _module
memoize_decorators = _module
np_utils = _module
path_utils = _module
query_params = _module
signal_decorators = _module
string_utils = _module
tz_utils = _module
units = _module
urls_utils = _module
validation = _module
workers_utils = _module
setup = _module
tests = _module
conftest = _module
test_agents = _module
test_agent = _module
test_async_spawner = _module
test_spawner = _module
test_api = _module
test_authentication = _module
test_log_handler = _module
test_user = _module
test_builds = _module
test_builder = _module
test_dockerfile_generator = _module
test_cli = _module
test_auth = _module
test_check = _module
test_config = _module
test_docker = _module
test_operations = _module
test_projects = _module
test_version = _module
test_client = _module
test_impersonate = _module
test_polyaxon_client = _module
test_statuses = _module
test_config_reader = _module
test_manager = _module
test_reader = _module
test_connections = _module
test_aws = _module
test_aws_client = _module
test_s3_store = _module
test_azure = _module
test_azure_client = _module
test_azure_store = _module
test_gcp = _module
test_gc_client = _module
test_gcs_store = _module
test_schemas = _module
test_secret_resources = _module
test_deploy = _module
test_celery = _module
test_deployment = _module
test_email = _module
test_ingress = _module
test_intervals = _module
test_rbac = _module
test_security_context = _module
test_service = _module
test_ssl = _module
test_init = _module
test_init_auth = _module
test_init_code = _module
test_k8s = _module
fixtures = _module
test_crd = _module
test_lifecycles = _module
test_lifecycle = _module
test_managers = _module
test_base = _module
test_ignore = _module
test_polypod = _module
test_project = _module
test_run = _module
test_notifiers = _module
test_discord_webhook = _module
test_hipchat_webhook = _module
test_mattermost_webhook = _module
test_pagerduty_webhook = _module
test_slack_webhook = _module
test_webhook_notification = _module
test_operators = _module
test_compose = _module
test_conda = _module
test_helm = _module
test_kubectl = _module
test_pip = _module
test_parser = _module
test_polyaxonfile = _module
test_default = _module
test_polyaxonfile_pipelines = _module
test_polyaxonfile_typing = _module
test_specification = _module
test_polyboard = _module
test_events = _module
test_logging = _module
test_logging_parser = _module
test_logs = _module
test_polyflow = _module
test_cache = _module
test_components = _module
test_container = _module
test_dags = _module
test_environments = _module
test_image_validation = _module
test_io = _module
test_params = _module
test_mounts = _module
test_k8s_artifact_mounts = _module
test_notifications = _module
test_ops = _module
test_op_runs = _module
test_plugins = _module
test_schedules = _module
test_sidecars = _module
test_termination = _module
test_workflows = _module
test_bo = _module
test_early_stopping = _module
test_grid_search = _module
test_hyperband = _module
test_iterative = _module
test_matrix = _module
test_parallel = _module
test_random_search = _module
test_commun = _module
test_accelerators = _module
test_container_resources = _module
test_env_vars = _module
test_volumes = _module
test_contexts = _module
test_converters = _module
test_converter = _module
test_platform_converter = _module
test_platform_job_converter = _module
test_custom_resources = _module
base_kubeflow = _module
test_job_crd = _module
test_mpi_job_crd = _module
test_pytorch_job_crd = _module
test_service_crd = _module
test_tf_job_crd = _module
test_init_dockerfile = _module
test_init_git = _module
test_init_outputs = _module
test_init_store = _module
test_init_utils = _module
test_main = _module
test_main_container = _module
test_main_env_vars = _module
test_main_mounts = _module
test_main_secrets = _module
test_pods = _module
test_pod_spec = _module
test_resolvers = _module
test_core_resolver = _module
test_sidecar = _module
test_sidecar_container = _module
test_sidecar_utils = _module
test_specs = _module
test_contexts_spec = _module
test_polytune = _module
test_hyperopt_search = _module
test_mapping = _module
test_pql = _module
test_proxies = _module
test_defaults = _module
test_gateway = _module
test_generate = _module
test_streams = _module
test_cli_configurations = _module
test_client_configuration = _module
test_polypod_config = _module
test_types = _module
test_dockerfile = _module
test_interval = _module
test_monitor = _module
test_summaries = _module
test_stores = _module
test_local_store = _module
test_artifact_endpoint = _module
test_artifacts_endpoints = _module
test_artifacts_tree_endpoint = _module
test_events_endpoints = _module
test_main_endpoints = _module
test_notify_endpoint = _module
test_stores_manager = _module
test_tracking = _module
test_event_recorder = _module
test_event_resources = _module
test_event_values = _module
test_run_tracking = _module
test_transports = _module
test_http_transport = _module
test_periodic_transport = _module
test_threaded_transport = _module
test_transport = _module
test_utils = _module
test_date_utils = _module
test_enums = _module
test_humanize = _module
test_list_utils = _module
test_memoize = _module
test_path_utils = _module
test_string_utils = _module
test_units = _module
test_validation = _module
horovod = _module
mnist = _module
mxnet = _module
pytorch = _module
mnist = _module
synthetic_benchmark = _module
bidirectional_lstm = _module
model = _module
cnn_lstm = _module
pytorchjob = _module
mnist = _module
tfjob = _module
newsgroup = _module
random_forest = _module
sgd_classifier = _module
iris = _module
best_models = _module
get_or_create_project = _module
manage = _module
polyconf = _module
config_manager = _module
config_settings = _module
wsgi = _module
scheduler = _module
apps = _module
health = _module
runs = _module
case = _module
test_scheduler = _module
test_runs_prepare = _module
test_runs_set_artifacts = _module
test_runs_start = _module
test_runs_stop = _module
apis = _module
views = _module
patterns = _module
project_resources = _module
versions = _module
rest = _module
test_artifacts = _module
test_views = _module
test_project_resources = _module
test_runs_views = _module
test_runs = _module
test_versions = _module
coredb = _module
abstracts = _module
deleted = _module
describable = _module
diff = _module
nameable = _module
readme = _module
runtime = _module
state = _module
status = _module
tag = _module
uid = _module
administration = _module
register = _module
methods = _module
queries = _module
serializers = _module
cloning = _module
tags = _module
subscriptions = _module
factories = _module
users = _module
run_time = _module
migrations = _module
singleton = _module
sub_paths = _module
unique_name = _module
models = _module
query_managers = _module
artifact = _module
callback_conditions = _module
signals = _module
test_artifacts_serializers = _module
test_project_resources_serializers = _module
test_projects_serializers = _module
test_runs_serializers = _module
test_executor = _module
test_exectuor = _module
test_executor_subscriptions = _module
test_query = _module
test_query_managers = _module
test_create_runs_manager = _module
test_run_model = _module
test_runs_manager = _module
test_runs_status_manager = _module
polycommon = _module
filters = _module
index = _module
paginator = _module
regex = _module
auditor = _module
polyaxon_task = _module
queues = _module
routes = _module
checks = _module
health_task = _module
results = _module
commands = _module
management = _module
create_exchange = _module
createuser = _module
conf_manager = _module
env_handler = _module
settings_handler = _module
option_manager = _module
option_service = _module
content_types = _module
crypto = _module
auditor_subscriptions = _module
event_actions = _module
event_context = _module
event_manager = _module
event_service = _module
event_subjects = _module
registry = _module
attributes = _module
json_utils = _module
memory_manager = _module
options = _module
conf_subscriptions = _module
installation = _module
stats = _module
feature = _module
option = _module
option_namespaces = _module
option_owners = _module
option_subjects = _module
query = _module
redis_db = _module
service_interface = _module
assets = _module
context_processors = _module
cors = _module
defaults = _module
encryption = _module
middlewares = _module
secrets = _module
test_cases = _module
jobs = _module
pipelines = _module
test_clients = _module
unique_urls = _module
user_system = _module
blacklist = _module
slugs = _module
test_auditor = _module
test_conf = _module
test_env_options_handler = _module
test_option_service = _module
test_config_manager = _module
test_attribute = _module
test_auditor_subscriptions = _module
test_event_context = _module
test_event_manager = _module
test_event_service = _module
test_events_registry = _module
test_gzip_decorator = _module
test_options = _module
test_conf_subscriptions = _module
test_feature = _module
test_option = _module
test_option_manager = _module
test_slugs = _module
test_unique_urls = _module
polyaxon_sdk = _module
access_resources_v1_api = _module
agents_v1_api = _module
artifacts_stores_v1_api = _module
auth_v1_api = _module
connections_v1_api = _module
dashboards_v1_api = _module
hub_components_v1_api = _module
hub_models_v1_api = _module
organizations_v1_api = _module
project_dashboards_v1_api = _module
project_searches_v1_api = _module
projects_v1_api = _module
queues_v1_api = _module
run_profiles_v1_api = _module
runs_v1_api = _module
schemas_v1_api = _module
searches_v1_api = _module
teams_v1_api = _module
users_v1_api = _module
versions_v1_api = _module
api_client = _module
configuration = _module
agent_state_response_agent_state = _module
notification_trigger = _module
protobuf_any = _module
protobuf_null_value = _module
runtime_error = _module
spark_deploy_mode = _module
v1_access_resource = _module
v1_agent = _module
v1_agent_state_response = _module
v1_agent_status_body_request = _module
v1_artifact_kind = _module
v1_artifact_tree = _module
v1_artifacts_mount = _module
v1_artifacts_type = _module
v1_auth = _module
v1_auth_type = _module
v1_average_stopping_policy = _module
v1_bayes = _module
v1_bucket_connection = _module
v1_cache = _module
v1_claim_connection = _module
v1_clean_pod_policy = _module
v1_cloning = _module
v1_cloning_kind = _module
v1_compiled_operation = _module
v1_component = _module
v1_connection_kind = _module
v1_connection_response = _module
v1_connection_schema = _module
v1_connection_type = _module
v1_credentials = _module
v1_cron_schedule = _module
v1_dag = _module
v1_dag_ref = _module
v1_dashboard = _module
v1_dask = _module
v1_diff_stopping_policy = _module
v1_dockerfile_type = _module
v1_early_stopping = _module
v1_entities_tags = _module
v1_entity_notification_body = _module
v1_entity_status_body_request = _module
v1_environment = _module
v1_event = _module
v1_event_artifact = _module
v1_event_audio = _module
v1_event_chart = _module
v1_event_chart_kind = _module
v1_event_curve = _module
v1_event_curve_kind = _module
v1_event_dataframe = _module
v1_event_histogram = _module
v1_event_image = _module
v1_event_model = _module
v1_event_type = _module
v1_event_video = _module
v1_events_response = _module
v1_exact_time_schedule = _module
v1_failure_early_stopping = _module
v1_flink = _module
v1_gcs_type = _module
v1_git_connection = _module
v1_git_type = _module
v1_grid_search = _module
v1_host_connection = _module
v1_host_path_connection = _module
v1_hp_choice = _module
v1_hp_geom_space = _module
v1_hp_lin_space = _module
v1_hp_log_normal = _module
v1_hp_log_space = _module
v1_hp_log_uniform = _module
v1_hp_normal = _module
v1_hp_p_choice = _module
v1_hp_params = _module
v1_hp_q_log_normal = _module
v1_hp_q_log_uniform = _module
v1_hp_q_normal = _module
v1_hp_q_uniform = _module
v1_hp_range = _module
v1_hp_uniform = _module
v1_hub_component = _module
v1_hub_model = _module
v1_hub_ref = _module
v1_hyperband = _module
v1_hyperopt = _module
v1_hyperopt_algorithms = _module
v1_image_type = _module
v1_init = _module
v1_interval_schedule = _module
v1_io = _module
v1_io_cond = _module
v1_iterative = _module
v1_job = _module
v1_k8s_resource_schema = _module
v1_k8s_resource_type = _module
v1_kf_replica = _module
v1_list_access_resources_response = _module
v1_list_agents_response = _module
v1_list_connections_response = _module
v1_list_dashboards_response = _module
v1_list_hub_components_response = _module
v1_list_hub_models_response = _module
v1_list_organization_members_response = _module
v1_list_organizations_response = _module
v1_list_projects_response = _module
v1_list_queues_response = _module
v1_list_run_artifacts_response = _module
v1_list_run_profiles_response = _module
v1_list_runs_response = _module
v1_list_searches_response = _module
v1_list_team_members_response = _module
v1_list_teams_response = _module
v1_log = _module
v1_log_handler = _module
v1_logs = _module
v1_mapping = _module
v1_matrix = _module
v1_matrix_kind = _module
v1_median_stopping_policy = _module
v1_metric_early_stopping = _module
v1_mpi_job = _module
v1_notification = _module
v1_operation = _module
v1_operation_body = _module
v1_operation_cond = _module
v1_optimization = _module
v1_optimization_metric = _module
v1_optimization_resource = _module
v1_organization = _module
v1_organization_member = _module
v1_param = _module
v1_param_search = _module
v1_path_ref = _module
v1_pipeline = _module
v1_pipeline_kind = _module
v1_plugins = _module
v1_polyaxon_init_container = _module
v1_polyaxon_sidecar_container = _module
v1_project = _module
v1_project_entity_resource_request = _module
v1_project_settings = _module
v1_project_teams = _module
v1_pytorch_job = _module
v1_queue = _module
v1_random_search = _module
v1_ray = _module
v1_reference = _module
v1_repeatable_schedule = _module
v1_resource_type = _module
v1_run = _module
v1_run_artifact = _module
v1_run_artifacts = _module
v1_run_kind = _module
v1_run_profile = _module
v1_run_schema = _module
v1_run_settings = _module
v1_run_settings_catalog = _module
v1_s3_type = _module
v1_schedule = _module
v1_schemas = _module
v1_search = _module
v1_search_spec = _module
v1_service = _module
v1_spark = _module
v1_spark_replica = _module
v1_spark_type = _module
v1_status = _module
v1_status_cond = _module
v1_status_condition = _module
v1_statuses = _module
v1_team = _module
v1_team_member = _module
v1_termination = _module
v1_tf_job = _module
v1_trigger_policy = _module
v1_truncation_stopping_policy = _module
v1_uri_type = _module
v1_url_ref = _module
v1_user = _module
v1_uuids = _module
v1_version = _module
v1_versions = _module
v1_wasb_type = _module

from _paritybench_helpers import _mock_config, patch_functional
from unittest.mock import mock_open, MagicMock
from torch.autograd import Function
from torch.nn import Module
import abc, collections, copy, enum, functools, inspect, itertools, logging, math, numbers, numpy, queue, random, re, scipy, sklearn, string, tensorflow, time, torch, torchaudio, torchtext, torchvision, types, typing, uuid, warnings
import numpy as np
from torch import Tensor
patch_functional()
open = mock_open()
yaml = logging = sys = argparse = MagicMock()
ArgumentParser = argparse.ArgumentParser
_global_config = args = argv = cfg = config = params = _mock_config()
argparse.ArgumentParser.return_value.parse_args.return_value = _global_config
yaml.load.return_value = _global_config
sys.argv = _global_config
__version__ = '1.0.0'


import torch.nn as nn


import torch.nn.functional as F


import torch.optim as optim


from torchvision import datasets


from torchvision import transforms


import torch.utils.data.distributed


import torch.backends.cudnn as cudnn


from torchvision import models


import numpy as np


import torch


import torch.distributed as dist


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 20, 5, 1)
        self.conv2 = nn.Conv2d(20, 50, 5, 1)
        self.fc1 = nn.Linear(4 * 4 * 50, 500)
        self.fc2 = nn.Linear(500, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(x, 2, 2)
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, 2, 2)
        x = x.view(-1, 4 * 4 * 50)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)

