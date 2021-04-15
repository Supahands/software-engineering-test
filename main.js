const { getSeedData, sortLoginTimestamp, findConsecutiveLogins } = require('./processor');

main();

async function main() {
    // in case the file name is different, please modify it accordingly
    const PYTHON_SEEDER_FILE_PATH = `${__dirname}/seed.py`;
    const seedData = await getSeedData(PYTHON_SEEDER_FILE_PATH);

    const sortedLoginTimestamps = sortLoginTimestamp(seedData);

    // count the login consecutive and sort accordinglyz
    const results = findConsecutiveLogins(sortedLoginTimestamps);

    console.table(results, ['start','end', 'length']);
}

