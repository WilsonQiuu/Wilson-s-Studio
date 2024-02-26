// Check if dark mode is enabled
const isDarkMode = localStorage.getItem('darkMode') === 'true';
if (isDarkMode) {
    document.body.classList.add('dark-mode');
}

// Function to toggle dark mode
function toggleDarkMode() {
    const body = document.body;
    const isDarkMode = body.classList.contains('dark-mode');

    if (isDarkMode) {
        body.classList.remove('dark-mode');
        localStorage.setItem('darkMode', false);
    } else {
        body.classList.add('dark-mode');
        localStorage.setItem('darkMode', true);
    }

}
function goBack() {
    if (document.getElementById('sensei').style.display === 'block') {
        document.getElementById('sensei').style.display = 'none';
        document.getElementById('students').style.display = 'block';
    }
    // if we are on the students page, go back to the times page
    else if (document.getElementById('students').style.display === 'block') {
        document.getElementById('students').style.display = 'none';
        document.getElementById('times').style.display = 'block';
    }

}

let scheduledTimes = {};




// Function to populate the times
function populateTimes() {
    const timeList = document.getElementById('timeList');
    Object.keys(scheduledTimes).forEach(time => {
        const listItem = document.createElement('li');
        listItem.textContent = time;
        listItem.addEventListener('click', () => showStudents(time));
        timeList.appendChild(listItem);
    });

}

function showStudents(time) {
    const studentList = document.getElementById('studentList');
    studentList.innerHTML = ''; // Clear previous student list

    const studentsForTime = scheduledTimes[time];

    // Sort students by their first names
    studentsForTime.sort((a, b) => {
        const nameA = Object.keys(a)[0].split(' ')[0].toLowerCase(); // Get first name of student A
        const nameB = Object.keys(b)[0].split(' ')[0].toLowerCase(); // Get first name of student B
        return nameA.localeCompare(nameB);
    });

    studentsForTime.forEach(student => {
        const studentName = Object.keys(student)[0];
        const listItem = document.createElement('li');
        listItem.textContent = studentName;
        listItem.addEventListener('click', () => showSensei(studentName));
        studentList.appendChild(listItem);
    });

    // Hide times and show students
    document.getElementById('times').style.display = 'none';
    document.getElementById('students').style.display = 'block';
}

// Function to show Sensei for a selected student
function showSensei(studentName) {
    const senseiName = getSensiForStudent(studentName);

    // Display Sensei responsible for the selected student
    document.getElementById('senseiName').textContent = senseiName;

    // Hide students and show Sensei
    document.getElementById('students').style.display = 'none';
    document.getElementById('sensei').style.display = 'block';
}

function getSensiForStudent(studentName) {
    let sensei = 'Sensei not found';
    Object.values(scheduledTimes).forEach(students => {
        students.forEach(student => {
            if (Object.keys(student)[0] === studentName) {
                sensei = student[studentName];
            }
        });
    });

    return sensei;
}


// shows the stats of a sensei with the name of the sensei,
// their age and height
// stats for their orgranization, communication, problem solving, time management and leadder ship scores from 1 to 5 stars
// stats for a sensei is stored in a json file with the name of the sensei as a key and their states as an array of strings in the order of Sensei name (ex. "Sensei Josh"), age(ex. "20") , height(ex, "180cm"), organization (ex. "3"), communication (ex. "2"), problem solving (ex. "5"), time management (ex. "5") and leaddership scores (ex. "4")
function senseiCard(sensei) {

}


function updateList() {
    fetch('server/schedule.txt?v=' + Date.now()) // to make sure its the updated version
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(data => {
            scheduledTimes = JSON.parse(data);

            populateTimes();
        })
        .catch(error => {
            console.error('There was a problem fetching the schedule:', error);
        });
}

function searchStudents() {
    const searchValue = document.getElementById('searchInput').value.toLowerCase();
    const studentList = document.getElementById('studentList');

    studentList.innerHTML = '';

    Object.entries(scheduledTimes).forEach(([time, students]) => {
        students.forEach(student => {
            const studentName = Object.keys(student)[0].toLowerCase();
            const sensei = student[Object.keys(student)[0]];

            if (studentName.includes(searchValue)) {
                const listItem = document.createElement('li');
                listItem.textContent = `${studentName} (${sensei}) at ${time}`;
                studentList.appendChild(listItem);
            }
        });
    });
    document.getElementById('students').style.display = 'block';
    document.getElementById('times').style.display = 'none';
}

populateTimes();
updateList();