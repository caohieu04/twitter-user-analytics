import { React, useEffect, useState, useRef, useMountEffect } from 'react'
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
    controllers,
} from 'chart.js';
import Table from './Table';
// import ReactJson from 'react-json-view'
import { getTopicChart, getUserSimilarChart } from './Graph';
import { Line, Bar } from 'react-chartjs-2';
import { useScrollDirection, timeConverterMonthOnly } from './Utils';
import { styled } from '@mui/material/styles';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import twbg from './twitter_background.jpeg';

ChartJS.register(
    BarElement,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
);

const HOST = "skycore.site/entry"
const URL = "/v1/twitter/"
const SEARCH_OPTIONS = ['10ronaldinho', '50cent', 'actuallynph', 'adele', 'aliaa08', 'andresiniesta8', 'antanddec', 'anushkasharma', 'ashton5sos', 'avrillavigne', 'billgates', 'billnye', 'britneyspears', 'carlyraejepsen', 'channingtatum', 'chelseahandler', 'cherlloyd', 'chrisbrown', 'codysimpson', 'cristiano', 'cp3', 'danawhite', 'dollyparton', 'dylanobrien', 'eminem', 'greenday', 'hardwell', 'iamjamiefoxx', 'iamjhud', 'iamsteveharvey', 'ianmckellen', 'itsgabrielleu', 'janetjackson', 'jerryseinfeld', 'jessicasimpson', 'jessiej', 'joeygraceffa', 'johncena', 'johnlegend', 'kaka', 'katyperry', 'kellyrowland', 'kerrywashington', 'kevinjonas', 'khloekardashian', 'kyliejenner', 'leodicaprio', 'lewishamilton', 'linkinpark', 'littlemix', 'lucyhale', 'ludacris', 'luke5sos', 'magicjohnson', 'mariahcarey', 'martingarrix', 'metallica', 'michelleobama', 'mindykaling', 'neymarjr', 'niallofficial', 'nickcannon', 'nickjonas', 'oprah', 'ozzyosbourne', 'paramore', 'parishilton', 'paulmccartney', 'paulpierce34', 'pink', 'pitbull', 'priyankachopra', 'rainnwilson', 'realhughjackman', 'rickygervais', 'rioferdy5', 'rustyrockets', 'schwarzenegger', 'scottdisick', 'selenagomez', 'serenawilliams', 'shawnmendes', 'simonpegg', 'srbachchan', 'thebeatles', 'thevampsband', 'tigerwoods', 'tip', 'tonyhawk', 'tripleh', 'tyga', 'usainbolt', 'victoriabeckham', 'wizkhalifa', 'wossy', 'yengpluggedin', 'zooeydeschanel']

const Item = styled(Paper)(({ theme }) => ({
    backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : 'rgba(29,161,242,0.1)',
    // ...theme.typography.body2,
    // padding: theme.spacing(1),
    textAlign: 'center',
    color: theme.palette.text.secondary,
    height: "100%",
    // display: "flex",
    fontFamily: 'Comic Sans MS',
    alignItems: "center"
}));

function RenderReport(report, setTWID, tfv, setTfv, scrollState) {
    return (
        <div div className="container">
            <Grid container spacing={2}>
                <Grid item xs={12} ref={scrollState.refs[0]}>
                    <Item>
                        {/* <TextField
                            fullWidth
                            autoFocus={true}
                            autoComplete='off'
                            inputProps={{ style: { textAlign: 'center' } }}
                            id="standard-search"
                            value={tfv}
                            label="Twitter ID"
                            type="search"
                            variant="standard"
                            placeholder="We found your cool pal ;)"
                            className="search-bar"
                            color="success"
                            onChange={e => setTfv(e.target.value)}
                            onKeyUp={e => (e.key === 'Enter' ? setTWID(e.target.value.toLowerCase()) : null)} /> */}
                        <Autocomplete
                            id="combo-box-demo"
                            options={SEARCH_OPTIONS}
                            noOptionsText='Not yet stalked'
                            sx={{
                                '& .MuiAutocomplete-input, & .MuiInputLabel-root': {
                                    textAlign: 'center',
                                    fontSize: 16
                                }
                            }}
                            onChange={(e, v) => setTfv(v)}
                            onKeyUp={e => (e.key === 'Enter' ? setTWID(e.target.value.toLowerCase()) : null)}
                            value={tfv}
                            fullWidth
                            autoHighlight
                            disableClearable
                            autoComplete='off'
                            // isOptionEqualToValue={(option, value) => option === value}
                            renderInput={(params) =>
                                <TextField
                                    {...params}
                                    autoFocus={true}
                                    placeholder="Found your person. Use <- and -> to navigate."
                                    color="success"
                                    id="standard-search"
                                    label="Twitter ID"
                                    type="search"
                                    variant="standard"
                                    className="search-bar"
                                />
                            }
                        />
                    </Item>
                </Grid>
                <Grid item xs={12} ref={scrollState.refs[1]}>
                    <Item><Table heading={report.tw_keyword_table_heading} body={report.tw_keyword_table_body} caption={report.tw_keyword_table_caption} /></Item>
                </Grid>
                <Grid item xs={12} ref={scrollState.refs[2]}>
                    <Item><Line options={report.tw_chart.options} data={report.tw_chart.data} /></Item>
                </Grid>
                <Grid item xs={12} ref={scrollState.refs[3]}>
                    <Item><Bar options={report.user_cluster_chart.options} data={report.user_cluster_chart.data} /></Item>
                </Grid>
                <Grid item xs={12} ref={scrollState.refs[4]}>
                    <Item><Bar options={report.user_identify_chart.options} data={report.user_identify_chart.data} /></Item>
                </Grid>
                <Grid item xs={12} ref={scrollState.refs[5]}>
                    <Item><Line options={report.fb_chart.options} data={report.fb_chart.data} /></Item>
                </Grid>

            </Grid>
        </div>
    )
}

function RenderLoading() {
}

function RenderDefault(setTWID, tfv, setTfv) {
    return (
        <div div className="container">
            <Grid container spacing={40}>
                <Grid item xs={12}>
                    <Item>
                        <Autocomplete
                            id="combo-box-demo"
                            options={SEARCH_OPTIONS}
                            noOptionsText='Not yet added'
                            sx={{
                                '& .MuiAutocomplete-input, & .MuiInputLabel-root': {
                                    textAlign: 'center',
                                    fontSize: 16
                                }
                            }}
                            onChange={(e, v) => setTfv(v)}
                            onKeyUp={e => (e.key === 'Enter' ? setTWID(e.target.value.toLowerCase()) : null)}
                            value={tfv}
                            fullWidth
                            autoHighlight
                            disableClearable
                            autoComplete='off'
                            // isOptionEqualToValue={(option, value) => option === value}
                            renderInput={(params) =>
                                <TextField
                                    {...params}
                                    autoFocus={true}
                                    placeholder="User you wish to know"
                                    id="standard-search"
                                    label="Twitter ID"
                                    type="search"
                                    variant="standard"
                                    className="search-bar"
                                />
                            }
                        />
                    </Item>
                </Grid >
                <Grid item xs={12}>
                    <Item></Item>
                </Grid>
                <Grid item xs={6}>
                    <Item></Item>
                </Grid>
                <Grid item xs={6}>
                    <Item></Item>
                </Grid>
                <Grid item xs={6}>
                    <Item></Item>
                </Grid>
                <Grid item xs={6}>
                    <Item></Item>
                </Grid>
            </Grid >
        </div >
    )
}

function RenderError(setTWID, tfv, setTfv) {
    return (
        <div div className="container">
            <Grid container spacing={40}>
                <Grid item xs={12}>
                    <Item>
                        {/* <TextField
                            fullWidth
                            autoFocus={true}
                            autoComplete='off'
                            inputProps={{ style: { textAlign: 'center' } }}
                            id="standard-search"
                            value={tfv}
                            label="Twitter ID"
                            type="search"
                            variant="standard"
                            placeholder="Can't find user, try again ;)"
                            color="warning"
                            className="search-bar"
                            onChange={e => setTfv(e.target.value)}
                            onKeyUp={e => (e.key === 'Enter' ? setTWID(e.target.value.toLowerCase()) : null)} /> */}
                        <Autocomplete
                            id="combo-box-demo"
                            options={SEARCH_OPTIONS}
                            noOptionsText='Not yet stalked'
                            sx={{
                                '& .MuiAutocomplete-input, & .MuiInputLabel-root': {
                                    textAlign: 'center',
                                    fontSize: 16
                                }
                            }}
                            onChange={(e, v) => setTfv(v)}
                            onKeyUp={e => (e.key === 'Enter' ? setTWID(e.target.value.toLowerCase()) : null)}
                            value={tfv}
                            fullWidth
                            autoHighlight
                            disableClearable
                            autoComplete='off'
                            // isOptionEqualToValue={(option, value) => option === value}
                            renderInput={(params) =>
                                <TextField
                                    {...params}
                                    autoFocus={true}
                                    placeholder="User deleted or deactivated. Please try again !"
                                    color="warning"
                                    id="standard-search"
                                    label="Twitter ID"
                                    type="search"
                                    variant="standard"
                                    className="search-bar"
                                />
                            }
                        />
                    </Item>
                </Grid >
                <Grid item xs={12}>
                    <Item></Item>
                </Grid>
                <Grid item xs={6}>
                    <Item></Item>
                </Grid>
                <Grid item xs={6}>
                    <Item></Item>
                </Grid>
                <Grid item xs={6}>
                    <Item></Item>
                </Grid>
                <Grid item xs={6}>
                    <Item></Item>
                </Grid>
            </Grid >
        </div >
    )
}

// function disableScrolling(){
//     var x=window.scrollX;
//     var y=window.scrollY;
//     window.onscroll=function(){window.scrollTo(x, y);};
// }

// function enableScrolling(){
//     window.onscroll=function(){};
// }

function RenderCondition(state, report, setTWID, tfv, setTfv, scrollState, setScrollState) {
    // const [scrollPosition, setScrollPosition] = useState(0);
    // const handleScroll = () => {
    //     const position = window.pageYOffset;
    //     setScrollPosition(position);
    // };
    const scrollWithKeys = (e) => {
        console.log(scrollState)
        if (e.code === "ArrowRight") {
            setScrollState({...scrollState, id: (scrollState.id + 1) % scrollState.refs.length})
        } else if (e.code === "ArrowLeft") {
            setScrollState({...scrollState, id: (scrollState.id - 1) % scrollState.refs.length})
        }
    }
    // const scrollUpdate = () => {
    //     let min_dist = null;
    //     let position = window.pageYOffset;
    //     let where = 0;
    //     scrollState.refs.forEach((ref, i) => {
    //         let r = ref.current.offsetTop
    //         if (min_dist == null) {
    //             min_dist = Math.abs(r - position)
    //             where = i
    //         } else if (Math.abs(r - position) < min_dist) {
    //             min_dist = Math.abs(r - position)
    //             where = i
    //         }
    //     })
    //     console.log(scrollState, min_dist)
    //     setScrollState({...scrollState, id: where})
    // }
    // const scrollNormal = () => {
    //     console.log(scrollState)
    //     var ref = scrollState.refs[scrollState.id];
    //     if (!scrollState.freeze && ref && ref.current != null) {
    //         let position = window.pageYOffset;
    //         console.log(position, " ", ref.current.offsetTop)
    //         if (position > ref.current.offsetTop + 3) {
    //             setScrollState({...scrollState, id: (scrollState.id + 1) % scrollState.refs.length, freeze: true})
    //             disableScrolling()
    //         } else if (position < ref.current.offsetTop - 3) {
    //             setScrollState({...scrollState, id: (scrollState.id - 1) % scrollState.refs.length, freeze: true})
    //             disableScrolling()
    //         }
    //     }
    // }
    useEffect(() => {
        window.addEventListener("keyup", scrollWithKeys)
        // window.addEventListener('scroll', scrollUpdate, {'passive': true})
        // window.addEventListener("scroll", () => {
        //     if (timer !== null) { clearTimeout(timer); }
        //     timer = setTimeout(() => { scrollNormal() }, 30);
        // }, false)
        const executeScroll = (ref) => {
            if (ref && ref.current != null) {
                ref.current.scrollIntoView({ behavior: "smooth", block: "start" })
            }
        };
        executeScroll(scrollState.refs[scrollState.id]);
        // setScrollState({...scrollState, freeze: false})
        return () => {
            window.removeEventListener("keyup", scrollWithKeys)
            // window.removeEventListener('scroll', scrollUpdate)
        };
    }, [scrollState.id])

    // useMountEffect(executeScroll); // Scroll on mount
    console.log(state);


    switch (state) {
        case 'loading':
            return <div>{RenderLoading(report)}</div>
        case 'report':
            return <div>{RenderReport(report, setTWID, tfv, setTfv, scrollState)}</div>
        case 'error':
            return <div>{RenderError(setTWID, tfv, setTfv)}</div>
        default:
            return <div>{RenderDefault(setTWID, tfv, setTfv)}</div>
    }
}


function Report() {
    const [twID, setTWID] = useState()
    const [tfv, setTfv] = useState(''); // text field value
    const [report, setReport] = useState()
    const [state, setState] = useState('default')
    const [scrollState, setScrollState] = useState({'id': 0, 'refs': [useRef(null), useRef(null), useRef(null), useRef(null), useRef(null), useRef(null)], 'freeze': false})

    useEffect(() => {
        console.log(twID)
        if (twID === "" || twID === undefined) {
            return
        }
        var requestURL = `https://${HOST}${URL}${twID}`
        console.log("[SENT] " + requestURL)
        fetch(requestURL, { referrerPolicy: "unsafe-url" })
            .then(res => res.json())
            .then(res => res.data).then(data => {
                let re = {}
                let timeline = data.twitter[0].timeline
                let tw_username = data.twitter[0].username
                // let tw_id = data.twitter[0]._id
                // let tw_databytime = data.twitter[0].data_by_time
                // let tw_kind_best = data.twitter[0].kind_best
                let tw_keyword = data.twitter[0].keyword_best
                let tw_topic = data.twitter[0].topic_best
                // let tw_evaluate = data.twitter[0].evaluate
                // let fb_databytime = data.facebook[0].data_by_time
                // let fb_keyword = data.facebook[0].keyword_best
                let user_identify = data.user_identify
                let user_cluster = data.user_cluster

                // re.evaluate_chart = getEvaluateChart(tw_evaluate)
                re.tw_chart = getTopicChart(tw_topic, timeline, ['User Interests Visualization', `${tw_username}`])

                let fb_topic = null 
                data.facebook.forEach(fb => {
                    if (fb._id === user_identify[0]._id) {
                        fb_topic = fb.topic_best
                    }
                })
                re.fb_chart = getTopicChart(fb_topic, timeline, ['User Interests Visualization', 'Matched Facebook account', `${user_identify[0].username}`])
                re.user_identify_chart = getUserSimilarChart(user_identify, 'Facebook Username', ['User Identification', 'Identify accounts cross-platform(Facebook)', `Most matched: ${user_identify[0].username}`])
                re.user_cluster_chart = getUserSimilarChart(user_cluster, 'Twitter Username', ['User Clustering', 'Cluster alike Twitter accounts', `Most similar: ${user_cluster[0].username}`])

                re.tw_keyword_table_heading = timeline.map(t => timeConverterMonthOnly(t))
                re.tw_keyword_table_body = [tw_keyword.map(t => t.slice(0, 10).join("\n"))]
                re.tw_keyword_table_caption = ['Keyword Extraction', `${tw_username}`]
                setReport(re)
                setTfv('')
                setState('report')
                setScrollState({...scrollState, id: 0, freeze: false})
            }
            )
            .catch(err => {
                console.log(err)
                setTfv('')
                setTWID('')
                setState('error')
            })
    }, [twID])

    return (
        < div className="container" >
            {RenderCondition(state, report, setTWID, tfv, setTfv, scrollState, setScrollState)}
        </div >
    );

}

export default Report;
