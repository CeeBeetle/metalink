import os
import subprocess
import ctypes
import sys

class MetaLink:
    def __init__(self):
        if not self.is_admin():
            self.run_as_admin()

    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def run_as_admin(self):
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

    def enhance_connectivity(self):
        print("Enhancing internet connectivity...")
        self.modify_tcp_parameters()
        self.flush_dns()
        self.optimize_network_adapter()

    def modify_tcp_parameters(self):
        print("Modifying TCP parameters...")
        tcp_commands = [
            "netsh int tcp set global autotuninglevel=normal",
            "netsh int tcp set global chimney=enabled",
            "netsh int tcp set global congestionprovider=ctcp",
            "netsh int tcp set global ecncapability=enabled",
            "netsh int tcp set global rss=enabled"
        ]
        for command in tcp_commands:
            subprocess.run(command, shell=True)

    def flush_dns(self):
        print("Flushing DNS cache...")
        subprocess.run("ipconfig /flushdns", shell=True)

    def optimize_network_adapter(self):
        print("Optimizing network adapter settings...")
        adapter_commands = [
            "netsh interface ipv4 set subinterface \"Ethernet\" mtu=1500 store=persistent",
            "netsh interface tcp set global autotuninglevel=highlyrestricted"
        ]
        for command in adapter_commands:
            subprocess.run(command, shell=True)

    def reset_network_settings(self):
        print("Resetting network settings to default...")
        subprocess.run("netsh int ip reset", shell=True)
        subprocess.run("netsh winsock reset", shell=True)

    def display_help(self):
        help_text = """
        MetaLink - Enhance Internet Connectivity and Network Performance
        
        Commands:
        - enhance: Enhance internet connectivity
        - reset: Reset network settings to default
        - help: Display this help message
        """
        print(help_text)

if __name__ == "__main__":
    metalink = MetaLink()
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        if command == "enhance":
            metalink.enhance_connectivity()
        elif command == "reset":
            metalink.reset_network_settings()
        elif command == "help":
            metalink.display_help()
        else:
            print("Unknown command. Use 'help' to see available commands.")
    else:
        metalink.display_help()