# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|

  # Use a basic Ubuntu install as the base
  config.vm.box = "lucid32"

  config.vm.network("33.33.33.10")

  config.vm.share_folder("v-root", "/vagrant", ".", :nfs => true)

  config.vm.forward_port("web", 8000, 8000)

  config.vm.provision :shell, :path => "update-lucid32.sh"

end
