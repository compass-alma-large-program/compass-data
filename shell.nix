# Nix shell for COMPASS data reduction
# Type `nix-shell` in this directory to open a shell with IMAGER installed.
# See https://nixos.org for more information.

with import (fetchTarball {
  url = "https://github.com/nixos/nixpkgs/archive/refs/tags/24.05.tar.gz";
  sha256 = "1lr1h35prqkd1mkmzriwlpvxcb34kmhc9dnr48gkm8hh089hifmx";
}) { };
let
  nur = import (fetchTarball {
    # 3.09-05 with a patch for uv_merge bug 
    url = "https://github.com/nix-community/NUR/archive/e73b0b963720fa2de9d11dc7ea6ab30d8d5163fd.tar.gz";
    sha256 = "1cy51nzj7n8jgylvb3aiqpcksg6bwsl5kvm6gwhskjy5bzlfjhd7";
  }) { inherit pkgs; };
  imager = nur.repos.smaret.imager;
in
pkgs.mkShell rec {
  buildInputs = [
    imager
  ];
}
