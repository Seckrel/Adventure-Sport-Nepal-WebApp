import { Grid } from '@material-ui/core';
import FacebookIcon from '@material-ui/icons/Facebook';
import InstagramIcon from '@material-ui/icons/Instagram';
import YouTubeIcon from '@material-ui/icons/YouTube';
import TwitterIcon from '@material-ui/icons/Twitter';
import { useStyles } from '../styles';

export default function SocialMedia() {
    const classes = useStyles();
    return (
        <Grid item md={4} xs={12}>
            <Grid container className={classes.itemTextCenter}>
                <Grid item xs={3}>
                    <FacebookIcon fontSize={'large'} />
                </Grid>
                <Grid item xs={3}>
                    <InstagramIcon fontSize={'large'} />
                </Grid>
                <Grid item xs={3}>
                    <YouTubeIcon fontSize={'large'} />
                </Grid>
                <Grid item xs={3}>
                    <TwitterIcon fontSize={'large'} />
                </Grid>
            </Grid>
        </Grid>
    )
}