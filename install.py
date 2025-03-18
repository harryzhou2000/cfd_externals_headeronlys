import os
import shutil


def record_version_install(f_install):
    def install_version(*args, **kwargs):
        f_install(args, kwargs)
        mod_install_path = args[1]
        ver = args[2]
        with open(
            os.path.join(mod_install_path, "__cfd_externals_version"), "r"
        ) as file:
            file.write(ver)

    return install_version


@record_version_install
def install_argparse(mod_path: str, mod_install_path: str, ver: str):
    shutil.copytree(
        os.path.join(mod_path, "include"),
        os.path.join(mod_install_path, "."),
        dirs_exist_ok=True,
    )
    shutil.copytree(
        os.path.join(mod_path, "module"),
        os.path.join(mod_install_path, "."),
        dirs_exist_ok=True,
    )


@record_version_install
def install_boost(mod_path: str, mod_install_path: str, ver: str):
    libs_base = os.path.join(mod_path, "libs")
    libsDirs = os.listdir(libs_base)
    for lib in libsDirs:
        lib_base_c = os.path.join(libs_base, lib)
        if not os.path.isdir(lib_base_c):
            continue
        shutil.copytree(
            os.path.join(lib_base_c, "include/boost"),
            os.path.join(mod_install_path, "."),
            dirs_exist_ok=True,
        )


def install_HO_repo(mod: str, mod_path: str, mod_install_path: str, ver: str):
    if mod == "argparse":
        install_argparse(mod_path, mod_install_path, ver)
    else:
        raise ValueError(f"{mod} nod supported")
