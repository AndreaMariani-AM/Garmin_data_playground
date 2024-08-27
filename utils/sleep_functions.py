import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

def plt_sleep(daily_sleep, colors):
	sns.set(font_scale = 1)
	sns.set_style(style='white')

	plt.figure(figsize=(10, 6))

	#sns.lineplot(data=daily_sleep, legend=False, palette=["#E69F00"])
	sns.scatterplot(x=daily_sleep.index, y=daily_sleep.value, legend=False, color=colors[0], label="Daily Sleep Quality")
	sns.lineplot(x=daily_sleep.index, y=daily_sleep.rolling_average, legend=False, label='28-day Average (Roll)')

	plt.ylabel(None)
	plt.xlabel(None)
	plt.legend()
	plt.tick_params(bottom=True, left=True)
	plt.title("Daily Sleep Quality over the last 21 months")
	sns.despine(offset=10, trim=True)

	ax = plt.gca()
	ax.xaxis.set_major_locator(mdates.MonthLocator())
	ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))

	plt.xticks(rotation=45, ha="right")

	plt.show()

# Convert time to hours, with 21:00 as the starting point
def convert_time(time_obj):
    hours_from_21 = time_obj.hour + time_obj.minute / 60 - 21
    return hours_from_21 if hours_from_21 >= 0 else hours_from_21 + 24

def plot_bedtime(df, title):
	plt.figure(figsize=(10, 6))
	sns.scatterplot(x=df.index, y=df["sleep_start_hours"], label="Sleep Start",color=["#E69F00"], style=df["day_type"])
	sns.scatterplot(x=df.index, y=df["sleep_end_hours"], label="Sleep End", color=["#56B4E9"],style=df["day_type"])

	# Formatting
	plt.title(f"{title}")
	plt.ylabel("Time of Day")
	plt.xlabel("Date")
	ax = plt.gca()
	ax.xaxis.set_major_locator(mdates.MonthLocator())
	ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
	plt.xticks(rotation=45, ha="right")
	plt.yticks(range(0, 24, 2), [f"{(h + 21) % 24:02d}:00" for h in range(0, 24, 2)])
	plt.ylim(0, 18)
	plt.tight_layout()
	plt.legend()
	plt.show()

# Annotate weekdays
def is_weekend(day):
    if day in ['Saturday', 'Sunday']:
        return 'Weekend'
    else:
        return 'Weekday'