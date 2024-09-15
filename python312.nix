{pkgs, lib, ft, ...}:

let
  mods = (import ./python-mods.nix {inherit ft lib;});
  generatePyOverrides = (import ./python-functions.nix {inherit lib;} ).generatePyOverrides;

in
pkgs.python312.override {
  packageOverrides = self: super: generatePyOverrides mods self super;
}
