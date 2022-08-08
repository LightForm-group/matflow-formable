# Change Log

## [0.1.14] - 2022.08.08

### Changed

- Use x-direction normal stress/strain in single crystal parameter optimisation instead of Von Mises to better align with experimental data
- Use VonMises(VolumeAverage) in yield function fitting `equivalent_plastic_strain` measure instead of VolumeAverage(VonMises).

## [0.1.13] - 2022.03.18

### Changed

- In snippet `optimise_SC_parameters_LM`, use VonMises(volume-averaged stress/strain) instead of volume-averaged(VonMises stress/strain).

## [0.1.12] - 2021.12.20

### Added

- Add `plastic_range` parameter to `get_tensile_test` task, which allows specifying the range of stress-strain data that should be considered in, for example, parameter fitting.

## [0.1.11] - 2021.11.09

### Added

- Add `cyclic_uniaxial` load case method to task `generate_load_case`
- Add `mixed` load case method to task `generate_load_case`

## [0.1.10] - 2021.08.07

### Fixed

- Fix extracting RVE data from `volume_element_response` created from recent DAMASK-v3a3 update.

## [0.1.9] - 2021.08.06

### Added

- Add option `strain_rate_modes` for task `generate_load_case` using method `plane_strain`.

## [0.1.8] - 2021.04.10

### Changed

- Support `initial_parameters` and `opt_parameters` (i.e. optimisation parameters, including specifying bounds on yield function fitting).

## [0.1.7] - 2020.12.16

### Added

- Add support for task: `get_tensile_test` using method `from_CSV`.
- Add support for task: `optimise_single_crystal_parameters` using method `levenberg_marquardt`.

## [0.1.6] - 2020.09.17

### Fixed

- Add missing package data to distribution

## [0.1.5] - 2020.09.17

### Added

- Add `fixed_parameters` option for yield function fitting.

## [0.1.4] - 2020.08.22

### Fixed

- Allow different dump frequencies for each load case.

## [0.1.3] - 2020.08.22

### Changed

- Add `dump_frequency` to load case generators.

## [0.1.2] - 2020.06.09

### Added

- Add `fit_yield_function`

### Changed

- Compatibility changes for the next version of Matflow.

## [0.1.1] - 2020.05.11

### Fixed

- Ensure function mapper functions return `dict`s

## [0.1.0] - 2020.05.09

- Initial version.
