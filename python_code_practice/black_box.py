import datetime
import time
import random
import matplotlib.pyplot as plt


class FDR:
    def __init__(self):
        self.fdr_filename = "flight_data.txt"

    def record_data(self, altitude, airspeed, heading):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.fdr_filename, "a") as fdr_file:
            fdr_file.write(f"Time: {timestamp}, Altitude: {altitude}, "
                           f"Airspeed: {airspeed}, Heading: {heading}\n")
        self.remove_old_data()

    def remove_old_data(self):
        current_time = datetime.datetime.now()
        one_day_ago = current_time - datetime.timedelta(days=1)
        with open(self.fdr_filename, "r+") as fdr_file:
            lines = fdr_file.readlines()
            fdr_file.seek(0)
            for line in lines:
                if "Time" not in line:
                    fdr_file.write(line)
                else:
                    data_time = datetime.datetime.strptime(
                        line.split(",")[0].split("Time: ")[1],
                        "%Y-%m-%d %H:%M:%S")
                    if data_time > one_day_ago:
                        fdr_file.write(line)


class CVR:
    def __init__(self):
        self.cvr_filename = "cockpit_voice.txt"

    def record_voice(self, voice_data):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.cvr_filename, "a") as cvr_file:
            cvr_file.write(f"Time: {timestamp}, Voice: {voice_data}\n")
        self.remove_old_data()

    def remove_old_data(self):
        current_time = datetime.datetime.now()
        one_day_ago = current_time - datetime.timedelta(days=1)
        with open(self.cvr_filename, "r+") as cvr_file:
            lines = cvr_file.readlines()
            cvr_file.seek(0)
            for line in lines:
                if "Time" not in line:
                    cvr_file.write(line)
                else:
                    data_time = datetime.datetime.strptime(
                        line.split(",")[0].split("Time: ")[1],
                        "%Y-%m-%d %H:%M:%S")
                    if data_time > one_day_ago:
                        cvr_file.write(line)


def plot_data(filename):
    times = []
    altitudes = []
    airspeeds = []
    headings = []
    with open(filename, "r") as file:
        for line in file:
            if "Time" in line:
                parts = line.split(",")
                print("check parts = ", parts)
                time_str = line.split(",")[0].split("Time: ")[1]
                times.append(datetime.datetime.strptime(
                    time_str, "%Y-%m-%d %H:%M:%S"))
                if 'Altitude' in parts[1]:
                    altitude = int(parts[1].split(":")[1].strip())
                    altitudes.append(altitude)
                if 'Airspeed' in parts[2]:
                    airspeed = int(parts[2].split(":")[1].strip())
                    airspeeds.append(airspeed)
                if 'Heading' in parts[3]:
                    heading = int(parts[3].split(":")[1].strip())
                    headings.append(heading)

    plt.figure(figsize=(10, 6))
    plt.subplot(3, 1, 1)
    plt.plot(times, altitudes, marker='o', linestyle='-')
    plt.title('Altitude')
    plt.xlabel('Time')
    plt.ylabel('Altitude (ft)')
    plt.grid(True)

    plt.subplot(3, 1, 2)
    plt.plot(times, airspeeds, marker='o', linestyle='-')
    plt.title('Airspeed')
    plt.xlabel('Time')
    plt.ylabel('Airspeed (knots)')
    plt.grid(True)

    plt.subplot(3, 1, 3)
    plt.plot(times, headings, marker='o', linestyle='-')
    plt.title('Heading')
    plt.xlabel('Time')
    plt.ylabel('Heading (degrees)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def main():
    fdr = FDR()
    cvr = CVR()

    # Simulated continuous recording
    while True:
        # Generate random flight data
        altitude = random.randint(10000, 40000)
        airspeed = random.randint(300, 600)
        heading = random.randint(0, 360)

        # Generate random cockpit voice message
        voice_messages = ["Clear for landing.",
                          "Altitude alert! Descend to 25000 feet.",
                          "Prepare for turbulence.",
                          "Cabin crew, prepare for takeoff."]
        voice_data = random.choice(voice_messages)

        # Simulated flight data and cockpit voice recording
        fdr.record_data(altitude, airspeed, heading)
        cvr.record_voice(voice_data)

        # Plot data
        plot_data(fdr.fdr_filename)
        # plot_data(cvr.cvr_filename)

        # Delay for 1 second (adjust as needed)
        time.sleep(1)


if __name__ == "__main__":
    main()
