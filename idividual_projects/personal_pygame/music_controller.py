# music_controller.py (WAV-only SoundPlayer version)
import os
import subprocess
import time
import shutil
import sys

def clear_line():
    sys.stdout.write("\033[2K")  # clear entire line
    sys.stdout.write("\r")       # return to start of line

class MusicController:
    
    def __init__(self, tracks):
        # Convert all paths to absolute
        self.tracks = {name: os.path.abspath(path) for name, path in (tracks or {}).items()}
        self.track_names = list(self.tracks.keys())

        # Main channel
        self.current_track = None
        self.current_path = None
        self.is_paused = False
        self._ps_proc = None

        # Channel 1
        self.current_track1 = None
        self.current_path1 = None
        self.is_paused1 = False
        self._ps_proc1 = None

        # Channel 2
        self.current_track2 = None
        self.current_path2 = None
        self.is_paused2 = False
        self._ps_proc2 = None

        # Channel 3
        self.current_track3 = None
        self.current_path3 = None
        self.is_paused3 = False
        self._ps_proc3 = None

        # Find PowerShell
        self._powershell = shutil.which("powershell") or shutil.which("powershell.exe")

    # WAV ONLY
    def _is_supported(self, path):
        return isinstance(path, str) and path.lower().endswith(".wav")

    def _find_by_basename(self, basename):
        for folder in (os.path.dirname(__file__), os.getcwd()):
            try:
                for item in os.listdir(folder):
                    if item.lower() == basename.lower():
                        return os.path.join(folder, item)
            except:
                pass
        return None

    def _stop_proc(self, proc_attr):
        proc = getattr(self, proc_attr)
        if proc:
            try:
                proc.terminate()
                time.sleep(0.05)
                if proc.poll() is None:
                    proc.kill()
            except:
                pass
            setattr(self, proc_attr, None)

    def _launch_ps_loop(self, path, slot):
        if not self._powershell:
            print("PowerShell not found.")
            return None

        safe = path.replace("'", "''")

        # Pure SoundPlayer loop
        ps_script = (
            f"& {{ $p = New-Object System.Media.SoundPlayer '{safe}'; "
            f"$p.Load(); $p.PlayLooping(); Start-Sleep -Seconds 999999 }}"
        )

        try:
            proc = subprocess.Popen(
                [self._powershell, "-NoProfile", "-WindowStyle", "Hidden", "-Command", ps_script],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            print(f"SoundPlayer loop started for channel {slot}: {path}")
            return proc
        except Exception as e:
            print(f"PowerShell start failed for channel {slot}: {e}")
            return None

    def _slot_attrs(self, slot):
        if slot == 'main':
            return {
                'proc_attr': '_ps_proc',
                'track_attr': 'current_track',
                'path_attr': 'current_path',
                'paused_attr': 'is_paused'
            }
        return {
            'proc_attr': f"_ps_proc{slot}",
            'track_attr': f"current_track{slot}",
            'path_attr': f"current_path{slot}",
            'paused_attr': f"is_paused{slot}"
        }

    def _play_slot(self, slot, name):
        attrs = self._slot_attrs(slot)
        track_attr = attrs['track_attr']
        path_attr = attrs['path_attr']
        proc_attr = attrs['proc_attr']
        paused_attr = attrs['paused_attr']

        if name not in self.tracks:
            print(f"Track '{name}' not configured.")
            return

        path = self.tracks[name]

        if not os.path.exists(path):
            alt = self._find_by_basename(os.path.basename(path))
            if alt:
                path = os.path.abspath(alt)
                self.tracks[name] = path
            else:
                print(f"File not found for '{name}': {path}")
                return

        if not self._is_supported(path):
            print("Only WAV supported:", path)
            return

        self._stop_proc(proc_attr)
        proc = self._launch_ps_loop(path, slot)

        if proc:
            setattr(self, proc_attr, proc)
            setattr(self, track_attr, name)
            setattr(self, path_attr, path)
            setattr(self, paused_attr, False)
            clear_line()
            print(f"Playing track: {name}")

    def _stop_slot(self, slot):
        attrs = self._slot_attrs(slot)
        self._stop_proc(attrs['proc_attr'])
        setattr(self, attrs['track_attr'], None)
        setattr(self, attrs['path_attr'], None)
        setattr(self, attrs['paused_attr'], False)
        print(f"Stopped channel {slot}.")

    def _pause_slot(self, slot):
        attrs = self._slot_attrs(slot)
        if not getattr(self, attrs['track_attr']):
            print(f"Nothing playing on channel {slot}.")
            return
        self._stop_proc(attrs['proc_attr'])
        setattr(self, attrs['paused_attr'], True)
        print(f"Paused channel {slot}.")

    def _resume_slot(self, slot):
        attrs = self._slot_attrs(slot)
        if not getattr(self, attrs['paused_attr']):
            print(f"Nothing to resume on channel {slot}.")
            return
        name = getattr(self, attrs['track_attr'])
        self._play_slot(slot, name)

    def _next_slot(self, slot):
        attrs = self._slot_attrs(slot)
        cur = getattr(self, attrs['track_attr'])
        if cur not in self.track_names:
            print(f"No current track on channel {slot}.")
            return
        idx = self.track_names.index(cur)
        next_name = self.track_names[(idx + 1) % len(self.track_names)]
        self._play_slot(slot, next_name)

    def _prev_slot(self, slot):
        attrs = self._slot_attrs(slot)
        cur = getattr(self, attrs['track_attr'])
        if cur not in self.track_names:
            print(f"No current track on channel {slot}.")
            return
        idx = self.track_names.index(cur)
        prev_name = self.track_names[(idx - 1) % len(self.track_names)]
        self._play_slot(slot, prev_name)

    # Main channel
    def play(self, name): self._play_slot('main', name)
    def pause(self): self._pause_slot('main')
    def resume(self): self._resume_slot('main')
    def stop(self): self._stop_slot('main')
    def next_track(self): self._next_slot('main')
    def prev_track(self): self._prev_slot('main')

    # Channel 1
    def play1(self, name): self._play_slot('1', name)
    def pause1(self): self._pause_slot('1')
    def resume1(self): self._resume_slot('1')
    def stop1(self): self._stop_slot('1')
    def next1(self): self._next_slot('1')
    def prev1(self): self._prev_slot('1')

    # Channel 2
    def play2(self, name): self._play_slot('2', name)
    def pause2(self): self._pause_slot('2')
    def resume2(self): self._resume_slot('2')
    def stop2(self): self._stop_slot('2')
    def next2(self): self._next_slot('2')
    def prev2(self): self._prev_slot('2')

    # Channel 3
    def play3(self, name): self._play_slot('3', name)
    def pause3(self): self._pause_slot('3')
    def resume3(self): self._resume_slot('3')
    def stop3(self): self._stop_slot('3')
    def next3(self): self._next_slot('3')
    def prev3(self): self._prev_slot('3')

    def stop_all(self):
        self.stop()
        self.stop1()
        self.stop2()
        self.stop3()
        print("Stopped all channels.")
