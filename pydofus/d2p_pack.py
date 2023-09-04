import os, tempfile, fnmatch, json
from collections import OrderedDict
from pydofus.d2p import D2PReader, D2PBuilder, InvalidD2PFile
from pydofus.swl import SWLReader, SWLBuilder, InvalidSWLFile


def pack_d2p(input_file, swl_mode, output_dir):
    base_name = os.path.basename(input_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    d2p_input = open(input_file, "rb")
    d2p_template = D2PReader(d2p_input)
    d2p_output = open(os.path.join(output_dir, base_name), "wb")
    d2p_builder = D2PBuilder(d2p_template, d2p_output)

    list_files = OrderedDict()

    rootPath = os.path.join(".", "temp", base_name)
    print(f"Packing {base_name} ...")

    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, "*.*"):
            path = os.path.join(root, filename)
            file = path.replace(rootPath + "\\", "").replace("\\", "/")
            object_ = {}

            if "swf" in file and swl_mode == "true":
                json_input = open(path.replace("swf", "json"), "r")
                swf_input = open(path, "rb")
                swl_output = tempfile.TemporaryFile()

                swl_data = json.load(json_input)
                swl_data["SWF"] = swf_input.read()

                swl_builder = SWLBuilder(swl_data, swl_output)
                swl_builder.build()

                swl_output.seek(0)
                object_["binary"] = swl_output.read()
                list_files[file.replace("swf", "swl")] = object_

                json_input.close()
                swf_input.close()
                swl_output.close()
            elif "json" in file and swl_mode == "true":
                continue
            else:
                new_file = open(path, "rb")
                object_["binary"] = new_file.read()
                new_file.close()
                list_files[file] = object_

    d2p_builder.files = list_files
    d2p_builder.build()

    d2p_input.close()
    d2p_output.close()
