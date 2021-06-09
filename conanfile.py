from conans import ConanFile, CMake


class ScopeguardConan(ConanFile):
    name = "scope-guard"
    version = "0.3.8"
    license = "MIT"
    author = "offa <offa@github>"
    url = "https://github.com.offa/scope-guard"
    description = "Implementation of Scoped Guards and Unique Resource as proposed in P0052."
    homepage = "https://github.com/offa/scope-guard"
    topics = ("cpp", "cpp17", "p0052", "scope-guard",
              "scope-exit", "scope-fail", "scope-success", "unique-resource", "cmake")
    no_copy_source = True
    exports = ["LICENSE"]
    _source_dir = "{}-{}".format(name, version)
    scm = {
        "type": "git",
        "subfolder": _source_dir,
        "url": "{}.git".format(homepage),
        "revision": f"v{version}"
    }
    requires = (
        "catch2/2.13.6",
        "trompeloeil/40"
    )
    options = {
        "unittest": ["ON", "OFF"],
        "enable_compat_header": ["ON", "OFF"]
    }
    default_options = (
        "unittest=ON",
        "enable_compat_header=OFF"
    )

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["UNITTEST"] = self.options.unittest
        cmake.definitions["ENABLE_COMPAT_HEADER"] = self.options.enable_compat_header
        cmake.configure(source_folder=self._source_dir, build_folder="build")
        return cmake

    def package(self):
        self.copy("LICENSE", dst="license")
        cmake = self._configure_cmake()
        cmake.install()
