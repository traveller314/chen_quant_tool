from math import log,exp,sqrt
from scipy import stats

def call(st,k,r,T,sigma):
    '''
    st,k,r,T,sigma(T以年为单位，天数应该除以365)
    '''
    d1 = (log(st/k)+(r+1/2*sigma)*T)/(sigma*sqrt(T))
    d2 = d1-sigma*sqrt(T)
    call = st*stats.norm.cdf(d1)-k*exp(-r*T)*stats.norm.cdf(d2)
    return call

def put(st,k,r,T,sigma):
    '''
    st,k,r,T,sigma(T以年为单位，天数应该除以365)
    '''
    d1 = (log(st/k)+(r+1/2*sigma)*T)/(sigma*sqrt(T))
    d2 = d1-sigma*sqrt(T)
    put = k*exp(-r*T)*stats.norm.cdf(-1*d2)-1*st*stats.norm.cdf(-1*d1)
    return put
def delta(st,k,r,T,sigma,n=1):
    '''
    n默认为1看涨期权的delta
    n为-1为看跌期权的delta
    '''
    d1 = (log(st/k)+(r+1/2*sigma)*T)/(sigma*sqrt(T))
    delta = n*stats.norm.cdf(n*d1)
    return delta

def gamma(st,k,r,T,sigma):
    '''
    期权gamma值
    '''
    d1 = (log(st/k)+(r+1/2*sigma)*T)/(sigma*sqrt(T))
    gamma = stats.norm.pdf(d1)/(st*sigma*sqrt(T))
    return gamma

def theta(st,k,r,T,sigma,n=1):
    '''
    n默认为1看涨期权的delta
    n为-1为看跌期权的delta
    '''
    d1 = (log(st/k)+(r+1/2*sigma)*T)/(sigma*sqrt(T))
    d2 = d1-sigma*sqrt(T)
    theta = -1*(st*stats.norm.pdf(d1)*sigma)/(2*sqrt(T))-n*r*k*exp(-r*T)*stats.norm.cdf(n*d2)
    return theta

def vega(st,k,r,T,sigma):
    d1 = (log(st/k)+(r+1/2*sigma)*T)/(sigma*sqrt(T))
    vega = st*sqrt(T)*stats.norm.pdf(d1)
    return vega