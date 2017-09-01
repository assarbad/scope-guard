# Scope Guard

[![Build Status](https://travis-ci.org/offa/scope-guard.svg?branch=master)](https://travis-ci.org/offa/scope-guard)
[![GitHub release](https://img.shields.io/github/release/offa/scope-guard.svg)](https://github.com/offa/scope-guard/releases)
[![License](https://img.shields.io/badge/license-GPLv3-yellow.svg)](LICENSE)
![C++](https://img.shields.io/badge/c++-14-green.svg)

Implementation of `scope_guard` and `unique_resource` as proposed in [**N3949**][1].


## Compatibility

This implemenation conforms to [N3949][1], except:

1. **Namespace:** Another namespace is used instead of `std`.
1. **Filenames:** The filenames contain a `.h` extension.

These deviations are necessary through standard requirements.


## Documentation

- [*N3949 - Scoped Resource - Generic RAII Wrapper for the Standard Library*][1] (P. Sommerlad, A. L. Sandoval)



## License

**GNU General Public License (GPL)**

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


[1]: http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2014/n3949.pdf
