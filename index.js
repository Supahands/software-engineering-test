const { spawn } = require('child_process');
const python = spawn('python', ['seed.py', 'node.js', 'python']);
python.stdout.on('data', function(data) {
    console.table("Results with seed.py file examples");
    var a = data.toString();
    a = a.replace(/'/g, '"');
    a = JSON.parse(a);
    var times = a;
    var series = {
        start: new Date(),
        end: new Date(),
        numberOfEntryTimes: 0,
    };
    const miltSecond = 1000;
    const second = 60;
    const minute = 60;
    const hour = 24;
    //Know the dates of entry
    const timeStampDate = times.map(time => time.split(" ")[0]);
    timeStampDate.sort();
    //Delete history of login recurrence
    const loginDateString = timeStampDate.filter(
        (date, index) => timeStampDate.indexOf(date) === index
    );

    const loginDate = loginDateString.map(date => new Date(date));
    console.log(loginDate);
    const seriesLogins = [];
    seriesLogins.unshift(series);
    let currentStartDate = new Date();
    let currentEndDate = new Date();
    let currentDuration = 0;
    for (let n = 0; n < loginDate.length; n++) {
        const lastDate = loginDate[n];
        const isLastOne = n === loginDate.length - 1;

        if (n === 0) {
            currentStartDate = lastDate;
            currentEndDate = lastDate;
            currentDuration = 1;
        }

        const nextLogin = isLastOne ? null : loginDate[n + 1];
        const diff_time = isLastOne ?
            0 :
            Math.abs(loginDate[n].getTime() - nextLogin.getTime());
        const diff_days = Math.ceil(
            diff_time / (miltSecond * second * minute * hour)
        );
        const is_consecutive_day = diff_days === 1;

        if (is_consecutive_day) {
            currentEndDate = lastDate;
            currentDuration = currentDuration + 1;
        } else {
            if (currentDuration > 1) {
                seriesLogins.push({
                    start: currentStartDate,
                    end: lastDate,
                    duration: currentDuration
                });
            }
            currentStartDate = nextLogin;
            currentEndDate = lastDate;
            currentDuration = 1;
        }
    }
    seriesLogins.sort((a, b) => b.duration - a.duration);
    const longestSeriesLogin = seriesLogins
        .filter(series => series.duration === seriesLogins[1].duration)
        .map(series => {
            /*   const inputFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSS'Z'");
              const outputFormat = new SimpleDateFormat("dd-MM-yyyy");
              const date = inputFormat.parse(seriesLogins[1].start);
              const formattedDate = outputFormat.format(date); */
            const startDateFinal = seriesLogins[1].start.toISOString().replace(/T/, '').replace(/\..+/, '').replace(/00:00:00/, '');;
            const endDateFinal = seriesLogins[1].end.toISOString().replace(/T/, '').replace(/\..+/, '').replace(/00:00:00/, '');

            return {
                start: startDateFinal,
                end: endDateFinal,
                length: series.duration
            };
        });
    const longestSeriesLoginFinal = longestSeriesLogin.filter(function(elem, pos) {
        return longestSeriesLogin.indexOf(elem) == pos;
    });

    console.table(longestSeriesLoginFinal);
});

console.table("Results with static example");

var times = ['2021-03-13 15:13:05', '2021-03-13 23:13:05', '2021-03-16 15:13:05', '2021-03-16 23:13:05', '2021-03-17 07:13:05', '2021-03-17 15:13:05', '2021-03-17 23:13:05', '2021-03-18 07:13:05', '2021-03-18 15:13:05'];

var series = {
    start: new Date(),
    end: new Date(),
    numberOfEntryTimes: 0,
};
const miltSecond = 1000;
const second = 60;
const minute = 60;
const hour = 24;
const timeStampDate = times.map(time => time.split(" ")[0]);
timeStampDate.sort();
const loginDateString = timeStampDate.filter(
    (date, index) => timeStampDate.indexOf(date) === index
);
const loginDate = loginDateString.map(date => new Date(date));

const seriesLogins = [];
seriesLogins.unshift(series);
let currentStartDate = new Date();
let currentEndDate = new Date();
let currentDuration = 0;
for (let n = 0; n < loginDate.length; n++) {
    const lastDate = loginDate[n];
    const isLastOne = n === loginDate.length - 1;

    if (n === 0) {
        currentStartDate = lastDate;
        currentEndDate = lastDate;
        currentDuration = 1;
    }

    const nextLogin = isLastOne ? null : loginDate[n + 1];
    const diff_time = isLastOne ?
        0 :
        Math.abs(loginDate[n].getTime() - nextLogin.getTime());
    const diff_days = Math.ceil(
        diff_time / (miltSecond * second * minute * hour)
    );
    const is_consecutive_day = diff_days === 1;

    if (is_consecutive_day) {
        currentEndDate = lastDate;
        currentDuration = currentDuration + 1;
    } else {
        if (currentDuration > 1) {
            seriesLogins.push({
                start: currentStartDate,
                end: lastDate,
                duration: currentDuration
            });
        }
        currentStartDate = nextLogin;
        currentEndDate = lastDate;
        currentDuration = 1;
    }
}
seriesLogins.sort((a, b) => b.duration - a.duration);
const longestSeriesLogin = seriesLogins
    .filter(series => series.duration === seriesLogins[1].duration)
    .map(series => {

        const startDateFinal = seriesLogins[1].start.toISOString().replace(/T/, '').replace(/\..+/, '').replace(/00:00:00/, '');;
        const endDateFinal = seriesLogins[1].end.toISOString().replace(/T/, '').replace(/\..+/, '').replace(/00:00:00/, '');

        return {
            start: startDateFinal,
            end: endDateFinal,
            length: series.duration
        };
    });
const longestSeriesLoginFinal = longestSeriesLogin.filter(function(elem, pos) {
    return longestSeriesLogin.indexOf(elem) == pos;
});

console.table(longestSeriesLoginFinal);