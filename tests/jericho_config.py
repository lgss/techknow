import os
import sys
import getopt


class JerichoConfig:
    __local_driver = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], "d:", ["driver="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o in ("-d", "--driver"):
            __local_driver = a

    @staticmethod
    def __getbool(name, default):
        value = os.getenv(name)
        if value:
            return value.lower() == "true"
        else:
            return default

    @property
    def src_bucket_name(self):
        return os.getenv("JER_SRC_BUCKET")

    @property
    def src_bucket_key_id(self):
        return os.getenv("JER_SRC_KEY_ID", os.getenv("AWS_ACCESS_KEY_ID"))

    @property
    def src_bucket_key(self):
        return os.getenv("JER_SRC_KEY", os.getenv("AWS_ACCESS_KEY"))

    @property
    def out_region(self):
        return os.getenv("JER_OUT_REGION", os.getenv("AWS_REGION"))

    @property
    def out_bucket_name(self):
        return os.getenv("JER_OUT_BUCKET")

    @property
    def out_bucket_key_id(self):
        return os.getenv("JER_OUT_KEY_ID", os.getenv("AWS_ACCESS_KEY_ID"))

    @property
    def out_bucket_key(self):
        return os.getenv("JER_OUT_KEY", os.getenv("AWS_ACCESS_KEY"))

    @property
    def use_slack(self):
        return self.__getbool("JER_ENABLE_SLACK", True) and os.getenv("JER_SLACK_ENDPOINT")

    @property
    def slack_endpoint(self):
        return os.getenv("JER_SLACK_ENDPOINT")

    @property
    def use_system_chrome(self):
        return self.__getbool("JER_USE_SYSTEM_CHROME", os.getenv("AWS_EXECUTION_ENV") is None)

    @property
    def load_env_from_file(self):
        return os.getenv("JER_USE_SYSTEM_CHROME", os.getenv("AWS_EXECUTION_ENV") is None)

    @property
    def function_root(self):
        return os.getenv("LAMBDA_TASK_ROOT", os.path.dirname(__file__))

    @property
    def working_dir(self):
        return "/tmp/"

    @property
    def tests_root(self):
        return self.working_dir + "tests/"

    @property
    def chromium_dir(self):
        return self.working_dir + "chrome/"

    @property
    def local_driver(self):
        return self.__local_driver


config = JerichoConfig()