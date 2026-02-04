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
    name = "directory_path",
    description = "Hello world directory path",
    typ = portal.ParameterType.STRING,
    defaultValue = "hello.txt",
    longDescription = "Filesystem directory path where the output of the 'hello-world' startup script will be created.")

pc.defineParameter(
    name="file_name",
    description="Name of output file",
    typ=portal.ParameterType.STRING,
    defaultValue="hello.txt",
    longDescription="Name of the file where the hello world script will write its output."
)

#
# *** FIRST REQUIRED CHANGE: Add a filename parameter here for where
# the output of the startup script will go. The `name` argument should
# be set to `file_name`. Use the `defineParameter()` call above as a
# template. Do not simply uncomment the line below. That will not work...
#
# pc.defineParameter(...)

# Process the parameters defined above
params = pc.bindParameters()

# Request a single "raw" (bare metal) PC (compute) node, and set some
# attributes based on globals defined above.
node = request.RawPC("n1")
if 'IMAGE_URN' in globals() and IMAGE_URN:
    node.disk_image = IMAGE_URN
if 'HARDWARE_TYPE' in globals() and HARDWARE_TYPE:
    node.hardware_type = HARDWARE_TYPE
# See below for the second change that needs to be made to this script.
if hasattr(params, "directory_path") and hasattr(params, "file_name"):
    #
    # *** SECOND REQUIRED CHANGE: Build up a 'startup_script' string
    # variable, consisting first of the SCRIPT_PATH global variable,
    # followed by a space, then the 'directory_path' profile
    # parameter, next a forward slash ('/'), then followed lastly by
    # the 'file_name' profile parameter.  Note that profile parameters
    # are stored as attributes of the `params` object returned by the
    # `pc.bindParameters()` call above. E.g., 'params.directory_path'.
    #
    # Note: Don't simply uncomment the line below; doing so will
    # result in a syntax error!
    #
    # startup_script = "{}  ...".format(SCRIPT_PATH, ..)
    startup_script = "{} {}/{}".format(
    	SCRIPT_PATH,
    	params.directory_path,
    	params.file_name)
    node.addService(pg.Execute(shell="bash", command=startup_script))

# The portal expects this function to be called a the end of a profile script.
pc.printRequestRSpec()
