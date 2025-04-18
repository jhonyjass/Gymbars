document.addEventListener('DOMContentLoaded', function () {
    const meses = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ];

    var options = {
        chart: {
            height: 350,
            type: 'area'
        },
        dataLabels: {
            enabled: false
        },
        stroke: {
            curve: 'smooth'
        },
        series: [{
            name: 'Ingresos',
            data: ingresos_mensuales.map(d => d.total)
        }],
        xaxis: {
            categories: ingresos_mensuales.map(d => `${meses[d.mes - 1]} ${d.año}`)
        },
        tooltip: {
            y: {
                formatter: function (val) {
                    return val.toLocaleString();
                }
            }
        }
    };

    var chart = new ApexCharts(document.querySelector("#graficaIngresosPorMes"), options);
    chart.render();
});

