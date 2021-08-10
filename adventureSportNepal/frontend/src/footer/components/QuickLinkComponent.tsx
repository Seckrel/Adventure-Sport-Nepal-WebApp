import { Grid, Typography, Box, Button } from '@material-ui/core';
import { Link } from 'react-router-dom';
import { useStyles } from '../styles';

interface QuickLinkInterface {
    name: string;
    link: string;
}

const QUICK_LINK: QuickLinkInterface[] = [
    { name: "Home", link: '/' },
    { name: 'All Expendition', link: "#" },
    { name: 'About Us', link: '#' },
    { name: 'FAQ', link: 'faq' },
    { name: 'Enquiry', link: '#' }
]


export default function QuickLink() {
    const classes = useStyles();

    return (
        <Grid item
            md={4}
            xs={12}
            className={classes.doubleSidedBoarder}
        >
            <Grid
                container
                spacing={2}
            >
                <Grid item xs={12} className={classes.itemTextCenter}>
                    <Box mb={2}>
                        <Typography variant={'h5'} component={'div'}>
                            {"Quick Links"}
                        </Typography>
                    </Box>
                </Grid>
                {QUICK_LINK.map((item: QuickLinkInterface) => (
                    <Grid item xs={12} className={classes.itemTextCenter}>
                        <Button
                            component={Link}
                            to={item.link}
                        >
                            <Typography variant={'subtitle1'} component={'div'}>
                                {item.name}
                            </Typography>
                        </Button>
                    </Grid>
                ))}
            </Grid>
        </Grid>
    )

}