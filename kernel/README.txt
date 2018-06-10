Use build_config.sh from fedora kernel spec repo:

https://src.fedoraproject.org/rpms/kernel.git

$ ./build_config.sh kernel-4.16.12

Copy kernel-4.16.12-x86_64.config as '.config' in the linux kernel source dirrectory.

make xconfig

Enable CONFIG_PREEMPT_RT_FULL (menu Processor type and features -> Preemption model -> Fully preemptible kernel).
Enable CONFIG_HZ_1000 (menu Processor type and features -> Timer frequency -> 1000 Hz).
Save the configuration file.

Copy back .config file into kernel-config-4.16.
