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
DEFAULT_SCRIPT_PATH = "{}/bin/hello_world.sh".format(LOCAL_REPO_DIR)

# Top level objects needed to create other profile constructs
pc = portal.Context()
request = pc.makeRequestRSpec()

# Add a parameter for the startup script path.
pc.defineParameter(
    "script_path",
    "Startup script location",
    portal.ParameterType.STRING, DEFAULT_SCRIPT_PATH,
    longDescription="Filesystem path where the startup script lives. '/local/repository' the location of the local copy of the Git repository for the profile that was used to instantiate this experiment.")

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
if hasattr(params, "script_path") and hasattr(params, "file_name"):
    #
    # Build up a 'startup_script' variable here consisting of the 'script_path'
    # parameter, followed by a space, followed by the 'file_name' parameter.
    #
    # startup_script = ...
    node.addService(pg.Execute(shell="bash", command=startup_script))

# The portal expects this function to be called a the end of a profile script.
pc.printRequestRSpec()
