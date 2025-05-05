# Nix shell for COMPASS data reduction
# Type `nix-shell` in this directory to open a shell with IMAGER installed.
# See https://nixos.org for more information.

with import (fetchTarball {
  url = "https://github.com/nixos/nixpkgs/archive/refs/heads/nixos-24.11.tar.gz";
}) { };
let
  nur = import (fetchTarball {
    # IMAGER 4.4-01 with a patch to fix the CLEAN segfault
    # See https://forge.oasu.u-bordeaux.fr/ums-porea/projets/imager/alma_imager/-/issues/1
    url = "https://github.com/nix-community/NUR/archive/28a5ad53c9444a94f56041a685a446680905b19f.tar.gz";
    sha256 = "sha256:16ny9rqmfpr1ic762as8slsrj79ksfzsc4d4cxghx4lnl4mqc1s8";
  }) { inherit pkgs; };
  imager = nur.repos.smaret.imager;
in
pkgs.mkShell rec {
  buildInputs = [
    imager
  ];
}
