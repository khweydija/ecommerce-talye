const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
const map = L.map('map').setView([18.057692232222365, -16.01124241635209], 12);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);
var marker = L.marker([18.057692232222365, -16.01124241635209]).addTo(map);
var popup = marker.bindPopup('<b>Sidi Mohamed!</b><br />27666242.');
