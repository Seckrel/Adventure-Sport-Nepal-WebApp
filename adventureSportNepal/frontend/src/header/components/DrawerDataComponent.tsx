import {
    Box,
    IconButton,
    Divider,
    List,
    ListItem,
    ListItemText,
    Typography,
    Grid,
    Button
} from '@material-ui/core';
import { Fragment } from 'react';
import CloseIcon from '@material-ui/icons/Close';
import ArrowForwardIosIcon from '@material-ui/icons/ArrowForwardIos';

const ABOUTUS = [
    { name: "Our Team", items: [] },
    { name: "Safety", items: [] }
]

const InitMenu = ({ state, expeditionList, setState }: any) => {
    const handleClick = (name: string) => {
        switch (name) {
            case "EXPEDITION":
                setState((old: any) => [...old, expeditionList]);
                break;
            case "ABOUT US":
                setState((old: any) => [...old, ABOUTUS]);
                break;
            case "treking":
                setState((old: any) => [...old, expeditionList.find((obj: any) => obj.name == "treking").items]);
                break;
            case "treking":
                setState((old: any) => [...old, expeditionList.find((obj: any) => obj.name == "sking").items]);
                break;
        }
    }
    return (
        <List>
            {state.at(-1).map((s: any) => (
                <ListItem button onClick={() => handleClick(s.name)}>
                    <ListItemText primary={(s.name).toUpperCase()} />
                </ListItem>
            ))}
        </List>
    );
}


export default function DrawerData(props: any) {
    const { classes,
        handleDrawerToggle,
        state,
        setState,
        expeditionList } = props;

    const goBack = () => {
        state.splice(-1, 1);
        console.log("eunning", state);
        setState([...state]);
    }

    return (
        <Fragment>
            {console.log(state)}
            <Grid container>
                <Grid item xs={12}>
                    {state.length > 1 &&
                        (<Button
                            onClick={goBack}
                        >
                            back </Button>)
                    }
                    <Button onClick={handleDrawerToggle}> X </Button>
                </Grid>
                <Grid item xs={12}>
                    <InitMenu
                        state={state}
                        setState={setState}
                        expeditionList={expeditionList}
                    />
                </Grid>
            </Grid>
        </Fragment>
    );

};