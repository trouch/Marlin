from os.path import join
from os.path import expandvars

Import("env", "projenv")

DESTINATION = expandvars("${PIOENV}-${VERSION}.hex")

CMD = " ".join([
    "cp",
    "'" + join("$BUILD_DIR","${PROGNAME}.hex") + "'",
    "'" + join("./firmwares/",DESTINATION) + "'",
    "||",
    ":"
])

env.AddPostAction(
	join("$BUILD_DIR","${PROGNAME}.hex"),
	env.VerboseAction(CMD, "Copying " + DESTINATION))

env.AddPostAction(
    join("$BUILD_DIR","${PROGNAME}.elf"),
    env.VerboseAction(CMD, "Copying " + DESTINATION))
    