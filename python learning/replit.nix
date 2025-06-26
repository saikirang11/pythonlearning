{ pkgs }: {
  deps = [
    pkgs.python39
    pkgs.python39Packages.pip
    pkgs.python39Packages.virtualenv
    pkgs.nodejs-18_x
    pkgs.nodePackages.npm
    pkgs.mysql80
    pkgs.git
  ];
} 