# Changelog

## [0.2.1] - 2024-11-03

### Changed

- Updated documentation to use from_items_with_priority instead of from_pairs
- Improved example clarity in documentation

## [0.2.0] - 2024-11-01

### Changed

- `extend()` method now only accepts sequences of items using self-priority
- Added new `extend_with_priority()` method for sequences of (item, priority) pairs
- Improved documentation and examples
- Added more comprehensive tests

### Fixed

- Clarified API to prevent confusion about priority handling

## [0.1.0] - 2024-11-01

### Added

- Initial release
- Basic PriorityQueue implementation
- Support for min-heap and max-heap
- Priority functions module
