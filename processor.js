const { existsSync } = require('fs');
const { spawn } = require('child_process');
const { format, differenceInDays, isValid } = require('date-fns');

// main business logic
exports.findConsecutiveLogins = (sortedTimestamps) => {
    return sortedTimestamps
        .reduce( (data, loginTimestamp) => {
            const formatted = format(loginTimestamp, 'yyyy-MM-dd')

            if (data.length === 0) {
                data.push({
                    start: formatted,
                    end: formatted,
                    date: loginTimestamp,
                    length: 1
                })
            } else {
                const previous = data[data.length -1];
                const diffDay = differenceInDays(loginTimestamp, previous.date)
                // means is not login consecutively.
                if (diffDay > 1) {
                    data.push({
                        start: formatted,
                        end: formatted,
                        date: loginTimestamp,
                        length: 1
                    })
                } else if (diffDay === 1){
                    previous.length += 1;
                    previous.end =  formatted;
                    previous.date = loginTimestamp;
                }
            }

            return data;
        },[])
        .sort( (a, b) => b.length - a.length);
}

// sort the login timestamp. Throw the error if provided timestamp format is invalid
exports.sortLoginTimestamp =(timestamps) => {
    return timestamps
        // assuming the date format is fix
        .map( dateString => {
            if (typeof dateString !== 'string') {
                throw new Error('Input has to be string');
            }

            const date = new Date(dateString.split(' ')[0]);

            if (!isValid(date)) {
                throw new Error(`Date seems awkward ${dateString}`);
            }

            return date;
        })
        .sort( (a,b) => a - b);
}

// helper function to run the python seed file and convert to array accordingly
exports.getSeedData = (pythonSeederFilePath) => {

    // need to make sure the file is available
    if (!existsSync(pythonSeederFilePath)) {
        throw new Error(`${pythonSeederFilePath} is not found`);
    }

    const command = spawn('python', [pythonSeederFilePath]);
    
    return new Promise( (resolve, reject) => {
        let output = '';

        command.stdout.on('data', data => {
            // append all output from stdout.
            // need to ensure all output capture by seeder, in case seeder has large output
            output += data.toString();
        }).on('close', () => {
            // complete output

            // replace single quote, due to single quote causing invalid json format
            const jsonString = output.toString().replace(/'/g, '"');
            try {
                // convert the data to array
                resolve(
                    JSON.parse(
                        jsonString
                    )
                );
            } catch(e) {
                // something wrong when parsing the json string.
                reject(e);
            }  
        })
        .on('error', err => {
            console.log('asdf');
            reject(err);
        })
    });
}
