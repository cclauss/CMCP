import runtime.lib.ssjb as ssjb
import runtime.obf.deobf as deobf
import json
import os

Config = {}

HEADER = """
  _____ __  __  _____ _____
 / ____|  \/  |/ ____|  __ \.
| |    | \  / | |    | |__) |
| |    | |\/| | |    |  ___/
| |____| |  | | |____| |
 \_____|_|  |_|\_____|_|

Created by Chibill as custom coded version of MCP.
CMCP stands for Chibill's MCP or Custom MCP.
Desinged for use with Enigma's mappings
"""


def read_config(rel_path="config.conf"):
    with open(os.path.join(os.getcwd(), rel_path)) as in_file:
        return json.load(in_file)

def deobfuscate():
    """Deobfuscates Minecraft using the setting supplied in the setting file. Then decompiles it"""

    print("""Config is targeting version {MC Verson} with a side of: {Side}
Using Enigma Mappings with there version being: {Mapping Version}
The editor files will be built for: {Editor}""".format(**Config))
    mcVersion = Config["MC Verson"]
    side = Config["Side"]
    deobf.downloadMCplusLibs(side, mcVersion)
    deobf.downloadDecompAndDeobf(Config)
    deobf.downloadMappings(mcVersion, Config["Mapping Version"], side)
    deobf.deobf(mcVersion, side, Config)
    deobf.decompile(side, Config)
    # deobf.editor(Config["Editor"])


if __name__ == "__main__":
    print(HEADER)
    print("Reading Config")
    Config = read_config()
    ssjb.registerTask("deobf", deobfuscate)
    ssjb.run()
