
{
description = "python nixos developer environment";


inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
};

outputs = { self, nixpkgs, ... }@inputs:
let
    inherit (self) outputs;


    #forAllSystems = nixpkgs.lib.genAttrs [
    
    # https://github.com/NixOS/nixpkgs/issues/44255
    #freetype_static = pkgs.freetype.overrideAttrs (oldArgs: { dontDisableStatic = true; });
    ft = pkgs.freetype.overrideAttrs (oldArgs: { dontDisableStatic = true; });
    lib = pkgs.lib;
    #ft = pkgs.freetype;

    myConfig = {
        allowBroken = true;
        permittedInsecurePackages = [
            "openssl-1.1.1w"
        ];
    
        packageOverrides = pkgs: {
          python312 = (import ./python312.nix {inherit pkgs lib ft;});
        };
    };

    # https://nixos.org/manual/nixpkgs/unstable/#how-to-override-a-python-package-for-all-python-versions-using-extensions
        

    system = "x86_64-linux";

    pkgs = (import nixpkgs {
        inherit system;
        config = myConfig;   
    });
    stdenv = pkgs.stdenv;

    forAllSystems = nixpkgs.lib.genAttrs [
        "x86_64-linux"
    ];


     nixpkgsFor = forAllSystems (system: import nixpkgs 
       {
         inherit system;
         config = myConfig;
         #overlays = [ self.overlays.default ];

       }
    );

    python-312 = self.packages.${system}.python-312;
    
    
in
{


     packages = forAllSystems (system:
     let 
        pkgs = nixpkgsFor.${system};
     in 
     {

       python-312 = (import ./python-312.nix {inherit pkgs;}); 
       
      
       python-312-pip = pkgs.python312.withPackages (ps: [
          ps.pip
          ps.virtualenv
       ]);

       #my-wkhtmltopdf = pkgs.wkhtmltopdf-bin;
       
     });


     devShells.${system}.default = pkgs.mkShell {
         
      buildInputs = [

        #my-wkhtmltopdf
        
      ];

      shellHook = ''
        #alias np="scripts/start_nginx_then_local_postgresql.sh"
        echo " "



        ln -sf ${python-312}/bin/python ./python


        
      '';

     };

};

#  # Executed by `nix run .#<name>`
#  apps."<system>"."<name>" = {
#    type = "app";
#    program = "<store-path>";
#  };
#  # Executed by `nix run . -- <args?>`
#  apps."<system>".default = { type = "app"; program = "..."; };
#
#  # Formatter (alejandra, nixfmt or nixpkgs-fmt)
#  formatter."<system>" = derivation;
#  # Used for nixpkgs packages, also accessible via `nix build .#<name>`
#  legacyPackages."<system>"."<name>" = derivation;
#  # Overlay, consumed by other flakes
#  overlays."<name>" = final: prev: { };
#  # Default overlay
#  overlays.default = final: prev: { };
#  # Nixos module, consumed by other flakes
#  nixosModules."<name>" = { config }: { options = {}; config = {}; };
#  # Default module
#  nixosModules.default = { config }: { options = {}; config = {}; };
#  # Used with `nixos-rebuild switch --flake .#<hostname>`
#  # nixosConfigurations."<hostname>".config.system.build.toplevel must be a derivation
#  nixosConfigurations."<hostname>" = {};
#  # Used by `nix develop .#<name>`
#  devShells."<system>"."<name>" = derivation;
#  # Used by `nix develop`
#  devShells."<system>".default = derivation;
#  # Hydra build jobs
#  hydraJobs."<attr>"."<system>" = derivation;
#  # Used by `nix flake init -t <flake>#<name>`
#  templates."<name>" = {
#    path = "<store-path>";
#    description = "template description goes here?";
#  };
#  # Used by `nix flake init -t <flake>`
#  templates.default = { path = "<store-path>"; description = ""; };


}

