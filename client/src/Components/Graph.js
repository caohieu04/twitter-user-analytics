import colorLib from '@kurkle/color';
import { timeConverterMonthOnly } from './Utils';

const GLOBAL_FONT = "Comic Sans MS"
const TITLE_FONT_SIZE = 24
const LEGEND_FONT_SIZE = 16
const AXIS_FONT_SIZE = 12
const COLORS = [
    '#4dc9f6',
    '#f67019',
    '#f53794',
    '#537bc4',
    '#acc236',
    '#166a8f',
    '#00a950',
    '#58595b',
    '#8549ba'
];

const getLegend = () => {
    return {
        position: 'top',
        labels: {
            font: {
                size: LEGEND_FONT_SIZE,
                family: GLOBAL_FONT
            },
            boxWidth: 60,
            boxHeight: LEGEND_FONT_SIZE,
            padding: 16
        }
    }
}

const getTitle = (title) => {
    return {
        display: true,
        text: title,
        font: {
            weight: 'bold',
            size: TITLE_FONT_SIZE,
            family: GLOBAL_FONT
        }
    }
}

export function color(index) {
    return COLORS[index % COLORS.length];
}

export function transparentize(value, opacity) {
    var alpha = opacity === undefined ? 0.5 : 1 - opacity;
    return colorLib(value).alpha(alpha).rgbString();
}

export const CHART_COLORS = {
    red: 'rgb(255, 99, 132)',
    orange: 'rgb(255, 159, 64)',
    yellow: 'rgb(255, 205, 86)',
    green: 'rgb(75, 192, 192)',
    blue: 'rgb(54, 162, 235)',
    purple: 'rgb(153, 102, 255)',
    grey: 'rgb(201, 203, 207)',
    celeste: 'rgb(181, 248, 254)',
    champagne_pink: 'rgb(252, 228, 216)',
    sea_green_crayola: 'rgb(16, 255, 203)',
    violet_red: 'rgb(247, 85, 144)',
    orange_yellow_crayola: 'rgb(251, 216, 127)',
    bistre: 'rgb(230, 170, 210)'
};

const NAMED_COLORS = [
    CHART_COLORS.red,
    CHART_COLORS.orange,
    CHART_COLORS.yellow,
    CHART_COLORS.green,
    CHART_COLORS.blue,
    CHART_COLORS.purple,
    CHART_COLORS.grey,
    CHART_COLORS.sea_green_crayola,
    CHART_COLORS.bistre,
    CHART_COLORS.orange_yellow_crayola,
    CHART_COLORS.celeste,
    CHART_COLORS.champagne_pink,
    CHART_COLORS.violet_red
];

export function namedColor(index) {
    return NAMED_COLORS[index % NAMED_COLORS.length];
}

var _seed = Date.now();

export function srand(seed) {
    _seed = seed;
}

export function rand(min, max) {
    _seed = (_seed * 9301 + 49297) % 233280;
    return min + (_seed / 233280) * (max - min);
}

export function addDataset(chart, datasetName) {
    const dsColor = namedColor(chart.data.datasets.length);
    const newDataset = {
        label: datasetName,
        backgroundColor: transparentize(dsColor, 0.5),
        borderColor: dsColor,
        data: [],
    };
    chart.data.datasets.push(newDataset);
}

export function addDatasets(chart, datasetNames) {
    datasetNames.forEach((datasetName) => addDataset(chart, datasetName));
}

export function addData(chart, label, dataPoints) {
    if (chart.data.datasets.length > 0) {
        chart.data.labels.push(label);

        for (let index = 0; index < chart.data.datasets.length; ++index) {
            chart.data.datasets[index].data.push(dataPoints[index]);
        }
    }
}

export function newChart() {
    return {
        data: {
            labels: [],
            datasets: [],
        }
    };
}

export const getTopicChart = (topic, timeline, title) => {
    let chart = newChart()
    addDatasets(chart, ['Business', 'Comedy', 'Entertainment', 'Food & Drink', 'Politic', 'Sport', 'Style & Beauty'])
    console.log(topic, timeline, title)
    for (let i = 0; i < timeline.length; i++) {
        let values = topic[i] == null ? Array(7).fill(0) : Object.values(topic[i])
        addData(chart, timeConverterMonthOnly(timeline[i]), values)
    }
    chart.options = {
        responsive: true,
        spanGaps: true,
        plugins: {
            legend: getLegend(),
            title: getTitle(title)
        },
        scales: {
            x: {
                ticks: {
                    font: {
                        weight: 'bold',
                        size: AXIS_FONT_SIZE,
                        family: GLOBAL_FONT
                    }
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Similarity',
                    font: {
                        weight: 'bold',
                        size: AXIS_FONT_SIZE,
                        family: GLOBAL_FONT
                    }
                },
                ticks: {  
                    font: {
                        weight: 'bold',
                        size: AXIS_FONT_SIZE,
                        family: GLOBAL_FONT
                    }
                }
            }
        }
    }
    return chart
}



export const getUserSimilarChart = (user_similar, y_name, title) => {
    let chart = newChart()
    let min_score = null
    let max_score = null
    user_similar.filter(u => u.similarity !== -1).forEach(u => {
        if (min_score == null || u.similarity < min_score) {
            min_score = u.similarity
        }
        if (max_score == null || u.similarity > max_score) {
            max_score = u.similarity
        }
    })
    if (min_score == null || max_score == null) {
        min_score = max_score = 0
    }
    user_similar.forEach(u => u.similarity = u.similarity === -1 ? min_score - (min_score / 1000) : u.similarity)
    // console.log("P184", min_score, user_identify.map(m => m.username), user_identify.map(m => m.similarity))
    addDatasets(chart, user_similar.map(m => m.username))
    addData(chart, y_name, user_similar.map(m => m.similarity))
    chart.options = {
        indexAxis: 'y',
        spanGaps: true,
        elements: {
            bar: {
                borderWidth: 2,
            },
        },
        responsive: true,
        plugins: {
            legend: {...getLegend(), boxWidth: 80, position: 'left'},
            title: getTitle(title)
        },
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Similarity',
                    font: {
                        weight: 'bold',
                        size: AXIS_FONT_SIZE,
                        family: GLOBAL_FONT
                    }
                },
                ticks: {  
                    font: {
                        weight: 'bold',
                        size: AXIS_FONT_SIZE,
                        family: GLOBAL_FONT
                    }
                },
                min: min_score - (max_score - min_score) * 0.05 - (min_score / 1000),
                max: max_score
            },
            y: {
                display: false,
            }
        }
    };
    return chart
}


// export const getEvaluateChart = (evaluate) => {
//     let chart = newChart()
//     addDatasets(chart, ['Multipartite Rank', 'Topic Rank', 'GSDMM', 'LDA', 'RAKE'])
//     let min_score = 1
//     let max_score = -1
//     Object.values(evaluate).filter(u => u !== -1).forEach(u => {
//         if (u < min_score) {
//             min_score = u
//         }
//         if (u > max_score) {
//             max_score = u
//         }
//     })
//     let values = Object.values(evaluate).map(u => u = u === -1 ? min_score - (min_score / 100) : u)
//     addData(chart, '', values)
//     chart.options = {
//         indexAxis: 'y',
//         elements: {
//             bar: {
//                 borderWidth: 2,
//             },
//         },
//         responsive: true,
//         plugins: {
//             legend: {
//                 position: 'top',
//                 labels: {
//                     fontFamily: GLOBAL_FONT,
//                     boxWidth: 20,
//                     boxHeight: 2
//                 }
//             },
//             title: {
//                 display: true,
//                 text: 'Keyword Extraction - Method Comparison',
//             },
//         },
//         scales: {
//             x: {
//                 min: min_score - (max_score - min_score) * 0.025 - (min_score / 100),
//                 max: max_score
//             },
//             y: {
//                 display: false
//             }
//         }
//     }
//     return chart
// }

// export function newChart() {
//     return {
//         data: {
//             labels: [],
//             datasets: [],
//         }
        // options: {
        //     responsive: true,
        //     title: {
        //         display: true,
        //         text: 'Chart.js Time Scale'
        //     }
        //     // scales: {
        //     //     xAxes: [{
        //     //         type: 'time',
        //     //         time: {
        //     //             unit: 'day'
        //     //         }
        //     //     }],
        //     //     yAxes: [{
        //     //         scaleLabel: {
        //     //             display: true,
        //     //             labelString: 'value'
        //     //         }
        //     //     }]
        //     // }
        // }
    // };
// }
