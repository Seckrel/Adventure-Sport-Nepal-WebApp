import { createStyles, Theme, makeStyles } from '@material-ui/core/styles';


export const useStyles = makeStyles((theme: Theme) =>
    createStyles({
        doubleSidedBoarder: {
            borderLeft: "2px solid #505050",
            borderRight: "2px solid #505050",
            [theme.breakpoints.down('sm')]: {
                border: "0",
            }
        },
        itemTextCenter: {
            textAlign: "center"
        }
    })
);