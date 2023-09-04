import os, shutil
from glob import glob
import tkinter
from tkinter import filedialog

from pydofus.d2p_pack import pack_d2p
from pydofus.d2p_unpack import unpack_d2p


def update_textures():
    assert os.path.exists("./textures"), "Texture folder not found"
    username = os.getlogin()
    gfx_path = f"C:\\Users\\{username}\\AppData\\Local\\Ankama\\Dofus\\content\\gfx"

    # If Dofus isn't installed in the standard location, ask the user to locate the root folder
    if not os.path.exists(gfx_path):
        tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
        folder_path = filedialog.askdirectory()
        gfx_path = os.path.join(folder_path, "content", "gfx").replace("\\", "/")

    items = glob(f"{gfx_path}\\items\\bitmap*.d2p")
    maps = glob(f"{gfx_path}\\maps\\worldmap*.d2p")[:2]
    print("Unpacking original textures ...")
    for item in items:
        unpack_d2p(item)
    for map in maps:
        unpack_d2p(map)

    print("Overwriting with new textures ...")
    upscale_textures = glob("./textures/*")
    for texture in upscale_textures:
        unpack_d2p(texture)

    for map in maps:
        pack_d2p(map, "false", "./output/maps/")
    for item in items:
        pack_d2p(item, "swl", "./output/items/")

    print("Overwriting original textures with new textures ...")
    shutil.copytree("./output/", gfx_path, dirs_exist_ok=True)

    print("Cleaning up ...")
    shutil.rmtree("./output")
    shutil.rmtree("./temp")

    print("Done!")


if __name__ == "__main__":
    try:
        update_textures()
    except Exception as e:
        print(e)
        input("Press enter to continue ...")
