import os
import shutil


def record_version_install(f_install):
    def install_version(*args, **kwargs):
        f_install(*args, **kwargs)
        mod_install_path = args[1]
        ver = args[2]
        with open(
            os.path.join(mod_install_path, "__cfd_externals_version"), "w"
        ) as file:
            file.write(ver)

    return install_version


@record_version_install
def install_argparse(mod_path: str, mod_install_path: str, ver: str):
    shutil.copytree(
        os.path.join(mod_path, "include"),
        os.path.join(mod_install_path, "include"),
        dirs_exist_ok=True,
    )
    shutil.copytree(
        os.path.join(mod_path, "module"),
        os.path.join(mod_install_path, "module"),
        dirs_exist_ok=True,
    )
    shutil.copy(
        os.path.join(mod_path, "LICENSE"),
        os.path.join(mod_install_path, "LICENSE"),
    )


@record_version_install
def install_boost(mod_path: str, mod_install_path: str, ver: str):
    libs_base = os.path.join(mod_path, "libs")
    libsDirs = os.listdir(libs_base)

    for lib in libsDirs:
        lib_base_c = os.path.join(libs_base, lib)
        if not os.path.isdir(lib_base_c):
            continue
        for subdir, subdir_dirs, subdir_files in os.walk(lib_base_c):
            if os.path.basename(subdir) == "include" and os.path.isdir(
                os.path.join(subdir, "boost")
            ):
                shutil.copytree(
                    os.path.join(subdir, "boost"),
                    os.path.join(mod_install_path, "boost"),
                    dirs_exist_ok=True,
                )


@record_version_install
def install_CGAL(mod_path: str, mod_install_path: str, ver: str):
    for subdir, subdir_dirs, subdir_files in os.walk(mod_path):
        if os.path.basename(subdir) == "include" and os.path.isdir(
            os.path.join(subdir, "CGAL")
        ):
            shutil.copytree(
                os.path.join(subdir, "CGAL"),
                os.path.join(mod_install_path, "include", "CGAL"),
                dirs_exist_ok=True,
            )


@record_version_install
def install_cppcodec(mod_path: str, mod_install_path: str, ver: str):
    shutil.copytree(
        os.path.join(mod_path, "cppcodec"),
        os.path.join(mod_install_path, "."),
        dirs_exist_ok=True,
    )
    shutil.copy(
        os.path.join(mod_path, "LICENSE"),
        os.path.join(mod_install_path, "LICENSE"),
    )


@record_version_install
def install_eigen(mod_path: str, mod_install_path: str, ver: str):
    shutil.copytree(
        os.path.join(mod_path, "Eigen"),
        os.path.join(mod_install_path, "Eigen"),
        dirs_exist_ok=True,
    )
    shutil.copytree(
        os.path.join(mod_path, "unsupported"),
        os.path.join(mod_install_path, "unsupported"),
        dirs_exist_ok=True,
    )
    shutil.copy(
        os.path.join(mod_path, "signature_of_eigen3_matrix_library"),
        os.path.join(mod_install_path, "signature_of_eigen3_matrix_library"),
    )
    shutil.copy(
        os.path.join(mod_path, "eigen3.pc.in"),
        os.path.join(mod_install_path, "eigen3.pc.in"),
    )
    for su in ["APACHE", "BSD", "GPL", "LGPL", "MINPACK", "MPL2", "README"]:
        shutil.copy(
            os.path.join(mod_path, f"COPYING.{su}"),
            os.path.join(mod_install_path, f"COPYING.{su}"),
        )


@record_version_install
def install_nanoflann(mod_path: str, mod_install_path: str, ver: str):
    shutil.copytree(
        os.path.join(mod_path, "include"),
        os.path.join(mod_install_path),
        dirs_exist_ok=True,
    )
    shutil.copy(
        os.path.join(mod_path, "COPYING"),
        os.path.join(mod_install_path, "COPYING"),
    )


@record_version_install
def install_nlohmann(mod_path: str, mod_install_path: str, ver: str):
    shutil.copytree(
        os.path.join(mod_path, "include/nlohmann"),
        os.path.join(mod_install_path, "nlohmann"),
        dirs_exist_ok=True,
    )
    shutil.copy(
        os.path.join(mod_path, "LICENSE.MIT"),
        os.path.join(mod_install_path, "LICENSE.MIT"),
    )


@record_version_install
def install_full_repo(mod_path: str, mod_install_path: str, ver: str):
    shutil.copytree(
        os.path.join(mod_path),
        os.path.join(mod_install_path, "."),
        dirs_exist_ok=True,
    )


install_cpptrace = install_full_repo
install_doxygen_awesome_css = install_full_repo
install_exprtk = install_full_repo
install_fmt = install_full_repo
install_pybind11 = install_full_repo


def install_HO_repo(mod: str, mod_path: str, mod_install_path: str, ver: str):
    # if mod == "argparse":
    #     installer = install_argparse
    # elif mod == "boost":
    #     installer = install_boost
    # else:
    #     raise ValueError(f"{mod} not supported")
    mod_name_c = mod.replace("-", "_")

    installer = globals()[f"install_{mod_name_c}"]

    installer(mod_path, mod_install_path, ver)


if __name__ == "__main__":
    import json

    with open("version_table.json", "r") as file:
        data = json.load(file)
        print(data)

    install_dir = "install"

    for repo, version in data.items():

        print(f"\n{'='*12}\nHandling: [{repo}, {version}]")

        install_HO_repo(repo, repo, os.path.join(install_dir, repo), version)
