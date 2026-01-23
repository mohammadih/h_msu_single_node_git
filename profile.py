"""
Allocate a single compute node and run a simple "hello world" script.

Instructions:
Modify this profile as instructed in the source below, then give it a try!
"""
import geni.portal as portal
import geni.rspec.pg as pg

# Global "constants"
IMAGE_URN = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD"
HARDWARE_TYPE = "d710"
LOCAL_REPO_DIR="/local/repository"
SCRIPT_PATH = "{}/bin/hello-world.sh".format(LOCAL_REPO_DIR)
DEFAULT_DIRECTORY_PATH = "/var/tmp"

# Top level objects needed to create other profile constructs
pc = portal.Context()
request = pc.makeRequestRSpec()

# Parameter specifying the directory path for the startup script's output file.
pc.defineParameter(
    "directory_path",
    "Hello world directory path",
    portal.ParameterType.STRING, DEFAULT_DIRECTORY_PATH,
    longDescription="Filesystem directory path where the output of the 'hello-world' startup script will be created.")

#
# Add a filename parameter here for where the output of the startup script
# will go. Call the parameter (first argument to `defineParameter`) 'file_name'.
#
# portal.context.defineParameter(...)

# Process the defined parameters
params = pc.bindParameters()

node = request.RawPC("n1")
if 'IMAGE_URN' in globals() and IMAGE_URN:
    node.disk_image = IMAGE_URN
if 'HARDWARE_TYPE' in globals() and HARDWARE_TYPE:
    node.hardware_type = HARDWARE_TYPE
if hasattr(params, "directory_path") and hasattr(params, "file_name"):
    #
    # Build up a 'startup_script' string variable here consisting of
    # the SCRIPT_PATH global variable, followed by a space, followed
    # by the 'directory_path' parameter, followed by a forward slash
    # ('/'), then followed lastly by the 'file_name' parameter.
    # Note that parameters are stored as attributes of the parameters
    # object. E.g., 'params.directory_path'
    #
    # startup_script = ...
    node.addService(pg.Execute(shell="bash", command=startup_script))

# The portal expects this function to be called a the end of a profile script.
pc.printRequestRSpec()
